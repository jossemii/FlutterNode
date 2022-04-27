from distutils.command.build import build
from threading import Thread
import threading
from time import sleep
import grpc, gateway_pb2, gateway_pb2_grpc, api_pb2_grpc, api_pb2, celaut_pb2

from main import FRONTIER, GATEWAY, RANDOM, SHA3_256, MOJITO, WALK, WALL
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

# Get solver cnf
def build_method(hash: str):
    service = next(client_grpc(
        method = gateway_pb2_grpc.GatewayStub(
                    grpc.insecure_channel(MOJITO + ':8090'),
                ).StartService,
        input = service_extended(hash = hash),
        indices_parser = gateway_pb2.Instance,
        partitions_message_mode_parser = True,
        indices_serializer = StartService_input,
        partitions_serializer = StartService_input_partitions_v1  # There it's not used.
    ))
    print('service -> ', service)

for s in [FRONTIER, WALL]:
    print('Go to build ', s)
    threading.Thread(
        target=build_method,
        args=(s,)
    ).start()