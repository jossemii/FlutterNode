from time import sleep
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2_grpc, api_pb2, celaut_pb2

from main import FRONTIER, GATEWAY, RANDOM, SHA3_256, MOJITO
from grpcbigbuffer import Dir, client_grpc
from gateway_pb2_grpcbf import StartService_input, StartService_input_partitions_v1

from main import RANDOM

def service_extended(hash):
    yield gateway_pb2.HashWithConfig(
        hash = celaut_pb2.Any.Metadata.HashTag.Hash(
            type = bytes.fromhex(SHA3_256),
            value = bytes.fromhex(hash)
        ),
        config = celaut_pb2.Configuration()
    )

    # Send partition model.
    yield ( 
        gateway_pb2.ServiceWithMeta,
        Dir('__registry__/'+hash)
    )

def get_grpc_uri(instance: celaut_pb2.Instance) -> celaut_pb2.Instance.Uri:
    for slot in instance.api.slot:
        #if 'grpc' in slot.transport_protocol.metadata.tag and 'http2' in slot.transport_protocol.metadata.tag:
            # If the protobuf lib. supported map for this message it could be O(n).
        for uri_slot in instance.uri_slot:
            if uri_slot.internal_port == slot.port:
                return uri_slot.uri[0]
    raise Exception('Grpc over Http/2 not supported on this service ' + str(instance))


g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel('localhost' + ':8090'),
)
import os, psutil
process = psutil.Process(os.getpid())
start_mem = process.memory_info().rss  # in bytes 


# Get solver cnf
random = next(client_grpc(
    method = g_stub.StartService,
    input = service_extended(hash = RANDOM),
    indices_parser = gateway_pb2.Instance,
    partitions_message_mode_parser = True,
    indices_serializer = StartService_input,
    partitions_serializer = StartService_input_partitions_v1  # There it's not used.
))

print('random -> ', random)

exit()

uri = get_grpc_uri(random.instance)
random_stub = api_pb2_grpc.RandomStub(
    grpc.insecure_channel(
        uri.ip + ':' + str(uri.port)
    )
)
random_token = random.token

solver = next(client_grpc(
    method = g_stub.StartService,
    input = service_extended(hash = FRONTIER),
    indices_parser = gateway_pb2.Instance,
    partitions_message_mode_parser = True,
    indices_serializer = StartService_input,
    partitions_serializer = StartService_input_partitions_v1  # There it's not used.
))

print('SOLVER -> ', solver)

uri = get_grpc_uri(solver.instance)

solver_stub = api_pb2_grpc.SolverStub(
    grpc.insecure_channel(
        uri.ip + ':' + str(uri.port)
    )
)
solver_token = solver.token

print('\n\n memory usage -> ', process.memory_info().rss - start_mem)
print(' SOLVER SERVICE -> ', uri)

print('\nwait...')
sleep(10)
print('\n\nTest it')
while True:
    cnf = next(client_grpc(
        method = random_stub.RandomCnf,
        indices_parser = api_pb2.Cnf,
        partitions_message_mode_parser = True,
        input = gateway_pb2.Empty()
    ))

    interpretation  = next(client_grpc(
        method=solver_stub.Solve,
        input=cnf,
        indices_serializer = api_pb2.Cnf,
        indices_parser=api_pb2.Interpretation,
        partitions_message_mode_parser = True
    ))

    print('Interpretation -> ', interpretation)