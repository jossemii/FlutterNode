import grpc, gateway_pb2, gateway_pb2_grpc, buffer_pb2, random

from main import GATEWAY
from grpcbigbuffer import client_grpc
from gateway_pb2_grpcbf import StartService_input, StartService_input_partitions


g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080'),
)

# Get solver cnf
one = True
for i in range(1):
    one = not one
    for m in client_grpc(
        method=g_stub.StartService,
        partitions_message_mode_parser=False,
        indices_parser=StartService_input,
        yield_remote_partition_dir_on_serializer=False,
        input=gateway_pb2.TokenMessage(token=str(random.randint(1, 9999)))

    ): 
        print('message --> ', m)