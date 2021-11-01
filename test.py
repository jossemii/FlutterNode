from time import sleep
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2_grpc, api_pb2, celaut_pb2

from main import GATEWAY, SHA3_256, WALL, RANDOM, client_grpc
from gateway_pb2_grpc_indices import StartService_indices

def service_extended(hash):
    any = api_pb2.celaut__pb2.Any()
    any.ParseFromString(open('__registry__/'+hash, 'rb').read())

    config = True
    for h in any.metadata.hashtag.hash:
        if config:  # Solo hace falta enviar la configuracion en el primer paquete.
            config = False
            yield gateway_pb2.HashWithConfig(
                hash = h,
                config = celaut_pb2.Configuration()
            )
        yield h



def get_grpc_uri(instance: celaut_pb2.Instance) -> celaut_pb2.Instance.Uri:
    for slot in instance.api.slot:
        #if 'grpc' in slot.transport_protocol.metadata.tag and 'http2' in slot.transport_protocol.metadata.tag:
            # If the protobuf lib. supported map for this message it could be O(n).
        for uri_slot in instance.uri_slot:
            if uri_slot.internal_port == slot.port:
                return uri_slot.uri[0]
    raise Exception('Grpc over Http/2 not supported on this service ' + str(instance))


g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080'),
)
import os, psutil, gc
for i in range(1, 10):
    process = psutil.Process(os.getpid())
    start_mem = process.memory_info().rss  # in bytes 
    # Get solver cnf
    solver = next(client_grpc(
        method=g_stub.StartService,
        output_field=gateway_pb2.Instance,
        input=service_extended(hash=WALL),
        indices_serializer=StartService_indices
    ))

    uri = get_grpc_uri(solver.instance)
    solver_stub = api_pb2_grpc.SolverStub(
        grpc.insecure_channel(
            uri.ip + ':' + str(uri.port)
        )
    )
    solver_token = solver.token

    print('\n\n memory usage -> ', process.memory_info().rss - start_mem)
    print(' SOLVER SERVICE -> ', uri)
    sleep(10) 



# Get random cnf
print('\n\nGet new services....')
random = next(client_grpc(
    method = g_stub.StartService,
    output_field=gateway_pb2.Instance,
    input=service_extended(hash=RANDOM),
    indices_serializer=StartService_indices
))

uri = get_grpc_uri(random.instance)
random_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(
        uri.ip + ':' + str(uri.port)
    )
)
random_token = random.token

print(' RANDOM SERVICE -> ', uri)
sleep(1)
cnf = next(client_grpc(
    method=random_stub.RandomCnf,
    input = api_pb2.Empty(),
    output_field=api_pb2.Cnf
))

print('CNF -> ', cnf)

interpretation  = next(client_grpc(
    method=solver_stub.Solve,
    input=cnf,
    output_field=api_pb2.Interpretation
))

print('Interpretation -> ', interpretation)
