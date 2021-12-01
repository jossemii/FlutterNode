from api_pb2 import ServiceWithMeta
import grpcbigbuffer, gateway_pb2_grpc, grpc, gateway_pb2, sys, buffer_pb2

from main import MOJITO


def compile(partitions_model, repo):
    stub = gateway_pb2_grpc.GatewayStub(
        grpc.insecure_channel(MOJITO+':8080')
    )

    return next(grpcbigbuffer.client_grpc(
        method = stub.Compile,
        input = gateway_pb2.CompileInput(
            repo = repo,
            partitions_model = partitions_model,
        ),
        indices_parser = gateway_pb2.ServiceWithMeta,
        partitions_parser = partitions_model,
        partitions_message_mode_parser = False
    ))

compile(
    partitions_model = buffer_pb2.Buffer.Head.Partition(),
    repo = sys.argv[1]
)