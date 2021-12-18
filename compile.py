from gateway_pb2_grpcbf import Compile_output_partitions_v1, Compile_output_partitions_v2
import grpcbigbuffer, gateway_pb2_grpc, grpc, gateway_pb2, sys, os

from main import MOJITO


def compile(partitions_model, partitions_message_mode_parser, repo):
    for b in grpcbigbuffer.client_grpc(
        method = gateway_pb2_grpc.GatewayStub(
                    grpc.insecure_channel('localhost'+':8080')
                ).Compile,
        input = gateway_pb2.CompileInput(
            repo = repo,
            partitions_model = partitions_model,
        ),
        indices_parser = gateway_pb2.CompileOutput,
        partitions_parser = partitions_model,
        partitions_message_mode_parser = partitions_message_mode_parser
    ): yield b

id = None
for b in compile(
    partitions_model = Compile_output_partitions_v1 if not len(sys.argv)>2 else Compile_output_partitions_v2,
    partitions_message_mode_parser = [True, False] if not len(sys.argv)>2 else [True, False, False],
    repo = sys.argv[1]
): 
    if b is gateway_pb2.CompileOutput: pass
    elif not id and type(b) is str: 
        id = b
        os.mkdir('__registry__/'+id)
    elif id: os.system('mv '+b+' '+'__registry__/'+id+'/')
    else: raise Exception('\nError with the compiler output.'+ str(b))