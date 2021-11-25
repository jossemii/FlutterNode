from time import sleep
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2_grpc, api_pb2, celaut_pb2

from main import FRONTIER, GATEWAY, RANDOM
from grpcbigbuffer import client_grpc
from gateway_pb2_grpcbf import StartService_input, StartService_input_partitions

FRONTIER = "01d030604fc89032faf57b399098db819f4ec776c0419e86cdaf64d2217014f7"

def service_extended(hash):
    any_p1 = api_pb2.celaut__pb2.Any()
    any_p1.ParseFromString(open('__registry__/'+hash+'/p1', 'rb').read())
    
    config = True
    for h in any_p1.metadata.hashtag.hash:
        if config:  # Solo hace falta enviar la configuracion en el primer paquete.
            config = False
            print('yield hash with config')
            yield gateway_pb2.HashWithConfig(
                hash = h,
                config = celaut_pb2.Configuration()
            )
            continue
        print('yield only hash')
        yield h
    
    # Send partition model.
    print('yield service with config')
    yield ( 
        gateway_pb2.ServiceWithConfig,
        gateway_pb2.ServiceWithConfig(
            service = any_p1,
            config = celaut_pb2.Configuration()
        ),
        '__registry__/'+hash+'/p2'
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
    grpc.insecure_channel(GATEWAY + ':8080'),
)
import os, psutil
process = psutil.Process(os.getpid())
start_mem = process.memory_info().rss  # in bytes 
# Get solver cnf
for i in range(1):
    try:
        it = client_grpc(
            method=g_stub.StartService,
            indices_parser=gateway_pb2.Instance,
            partitions_message_mode_parser=True,
            input=service_extended(hash=FRONTIER),
            indices_serializer=StartService_input,
            partitions_serializer=StartService_input_partitions
        )
        solver = next(it)

        print('solver -> ', solver)
        
        uri = get_grpc_uri(solver.instance)
        solver_stub = api_pb2_grpc.SolverStub(
            grpc.insecure_channel(
                uri.ip + ':' + str(uri.port)
            )
        )
        solver_token = solver.token

        print('\n\n memory usage -> ', process.memory_info().rss - start_mem)
        print(' SOLVER SERVICE -> ', uri)
    except Exception as e: print('eee -> ', e)


    continue
    # Get random cnf
    print('\n\nGet new services....')
    random = next(client_grpc(
        method = g_stub.StartService,
        output_field = gateway_pb2.Instance,
        input = service_extended(hash=RANDOM),
        indices_serializer = StartService_input,
        partitions_serializer = StartService_input_partitions
    ))

    uri = get_grpc_uri(random.instance)
    random_stub = api_pb2_grpc.RandomStub(
        grpc.insecure_channel(
            uri.ip + ':' + str(uri.port)
        )
    )
    random_token = random.token


    for i in range(10):
        print(' RANDOM SERVICE -> ', uri)
        sleep(1)
        cnf = next(client_grpc(
            method=random_stub.RandomCnf,
            input = api_pb2.Empty(),
            output_field=api_pb2.Cnf,
            mem_manager = lambda len: None,
        ))

        print('CNF -> ', cnf)

        interpretation  = next(client_grpc(
            method=solver_stub.Solve,
            input=cnf,
            output_field=api_pb2.Interpretation
        ))

        print('Interpretation -> ', interpretation)
