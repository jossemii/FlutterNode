from random import randint, random, choice
import sys
from threading import Thread
from time import sleep
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2_grpc, api_pb2, celaut_pb2, buffer_pb2

from main import FRONTIER, GATEWAY, RANDOM, REGRESION, SHA3_256, MOJITO, TEQUILA, WALK, WALL, WHISKY
from grpcbigbuffer import Dir, client_grpc
from gateway_pb2_grpcbf import StartService_input, StartService_input_partitions_v1


def generator(hash: str, mem_limit: int = 50*pow(10, 6)):
    try:
        yield gateway_pb2.HashWithConfig(
            hash = celaut_pb2.Any.Metadata.HashTag.Hash(
                type = bytes.fromhex(SHA3_256),
                value = bytes.fromhex(hash)
            ),
            config = celaut_pb2.Configuration(),
            min_sysreq = celaut_pb2.Sysresources(
                mem_limit = mem_limit
            )
        )
    except Exception as e: print(e)

    # Send partition model.
    yield ( 
        gateway_pb2.ServiceWithMeta,
        Dir('__registry__/'+hash)
    ) 
    
def service_extended(hash):
    for t in generator(hash=hash): yield t  


def get_grpc_uri(instance: celaut_pb2.Instance) -> celaut_pb2.Instance.Uri:
    for slot in instance.api.slot:
        #if 'grpc' in slot.transport_protocol.metadata.tag and 'http2' in slot.transport_protocol.metadata.tag:
            # If the protobuf lib. supported map for this message it could be O(n).
        for uri_slot in instance.uri_slot:
            if uri_slot.internal_port == slot.port:
                return uri_slot.uri[0]
    raise Exception('Grpc over Http/2 not supported on this service ' + str(instance))


g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY),
)

def exec(id: int, solver_hash: str):
    print(id,'  Go to use ', solver_hash)
    # Get solver cnf
    random = next(client_grpc(
        method = g_stub.StartService,
        input = service_extended(hash = RANDOM),
        indices_parser = gateway_pb2.Instance,
        partitions_message_mode_parser = True,
        indices_serializer = StartService_input,
        partitions_serializer = StartService_input_partitions_v1  # There it's not used.
    ))

    print('random ',id,' -> ', random)



    random_uri = get_grpc_uri(random.instance)
    random_stub = api_pb2_grpc.RandomStub(
        grpc.insecure_channel(
            random_uri.ip + ':' + str(random_uri.port)
        )
    )
    random_token = random.token

    solver = next(client_grpc(
        method = g_stub.StartService,
        input = service_extended(hash = solver_hash),
        indices_parser = gateway_pb2.Instance,
        partitions_message_mode_parser = True,
        indices_serializer = StartService_input,
        partitions_serializer = StartService_input_partitions_v1  # There it's not used.
    ))

    print('SOLVER ',id,' -> ', solver)

    solver_uri = get_grpc_uri(solver.instance)

    solver_stub = api_pb2_grpc.SolverStub(
        grpc.insecure_channel(
            solver_uri.ip + ':' + str(solver_uri.port)
        )
    )
    solver_token = solver.token

    print(' SOLVER SERVICE ',id,' -> ', solver_uri)

    print('\nwait.',id,' ..')
    sleep(10)
    print('\n\nTest it  ',id,' on ', solver_uri)
    for i in range(1):
        while True:
            try:
                cnf = next(client_grpc(
                    method = random_stub.RandomCnf,
                    indices_parser = api_pb2.Cnf,
                    partitions_message_mode_parser = True,
                    input = buffer_pb2.Empty()
                ))
                print('cnf -> ', cnf)
                break
            except Exception as e: 
                print('ERROR LAUNCHING CNF', str(e))
                sleep(2)

        while True:
            try:
                interpretation  = next(client_grpc(
                    method=solver_stub.Solve,
                    input=cnf,
                    indices_serializer = api_pb2.Cnf,
                    indices_parser=api_pb2.Interpretation,
                    partitions_message_mode_parser = True
                ))
                break
            except Exception as e: 
                print('ERROR LAUNCHING SOLVER', str(e))
                sleep(2)

        print('Interpretation  ',id,' -- ',i,' -> ', interpretation)
    sleep(30)
    print('Go to stop that  ',id,' .', random_token, solver_token)
    next(client_grpc(
        method = g_stub.StopService,
        input = gateway_pb2.TokenMessage(
            token = random_token
        ),
        indices_parser = buffer_pb2.Empty,
    ))
    next(client_grpc(
        method = g_stub.StopService,
        input = gateway_pb2.TokenMessage(
            token = solver_token
        ),
        indices_parser = buffer_pb2.Empty,
    ))
    print('Stopped ', id)

thread_list = []
for i in range(int(sys.argv[1])):
    t = Thread(
        target = exec,
        args=(i, choice([FRONTIER]))
    )
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
print('\n\n TEST PASSED.')