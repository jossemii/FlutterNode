import grpc, gateway_pb2, gateway_pb2_grpc, buffer_pb2

from main import GATEWAY
from grpcbigbuffer import client_grpc
from gateway_pb2_grpcbf import StartService_input, StartService_input_partitions


g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(GATEWAY + ':8080'),
)

# Get solver cnf
for m in client_grpc(
    method=g_stub.StartService,
    output_field=gateway_pb2.Instance,
    partitions_parser={1: [
        buffer_pb2.Buffer.Head.Partition(index={1: buffer_pb2.Buffer.Head.Partition(), 2: buffer_pb2.Buffer.Head.Partition()}),
        buffer_pb2.Buffer.Head.Partition(index={3: buffer_pb2.Buffer.Head.Partition()}),
    ]},
    input=gateway_pb2.TokenMessage(token='adkfn')
): 
    print('message --> ', m)
