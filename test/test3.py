# Test combine method.

import gateway_pb2_grpcbf, celaut_pb2, gateway_pb2, gateway_pb2_grpc
import grpc
import grpcbigbuffer
from grpcbigbuffer import Dir, client_grpc
from main import MOJITO, SHA3_256

def service_extended():

    # Send partition model.
    yield ( 
        gateway_pb2.ServiceWithMeta,
        Dir('__registry__/8e86f9461f83790bfc1be49543646447ab4704437957bb6c442b8d6a9308f2ac')
    )    

g_stub = gateway_pb2_grpc.GatewayStub(
    grpc.insecure_channel(MOJITO+':8090'),
)

random = next(client_grpc(
    method = g_stub.StartService,
    input = service_extended(),
    indices_parser = gateway_pb2.Instance,
    partitions_message_mode_parser = True,
    indices_serializer = gateway_pb2_grpcbf.StartService_input,
    partitions_serializer = gateway_pb2_grpcbf.StartService_input_partitions_v1
))