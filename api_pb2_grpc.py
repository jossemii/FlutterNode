# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2
import ipss_pb2 as ipss__pb2
import onnx_pb2 as onnx__pb2


class RandomStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RandomCnf = channel.unary_unary(
                '/Random/RandomCnf',
                request_serializer=api__pb2.Empty.SerializeToString,
                response_deserializer=api__pb2.Cnf.FromString,
                )


class RandomServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RandomCnf(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RandomServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RandomCnf': grpc.unary_unary_rpc_method_handler(
                    servicer.RandomCnf,
                    request_deserializer=api__pb2.Empty.FromString,
                    response_serializer=api__pb2.Cnf.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Random', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Random(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RandomCnf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Random/RandomCnf',
            api__pb2.Empty.SerializeToString,
            api__pb2.Cnf.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SolverStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartTrain = channel.unary_unary(
                '/Solver/StartTrain',
                request_serializer=api__pb2.Empty.SerializeToString,
                response_deserializer=api__pb2.Empty.FromString,
                )
        self.StopTrain = channel.unary_unary(
                '/Solver/StopTrain',
                request_serializer=api__pb2.Empty.SerializeToString,
                response_deserializer=api__pb2.Empty.FromString,
                )
        self.GetTensor = channel.unary_stream(
                '/Solver/GetTensor',
                request_serializer=api__pb2.Empty.SerializeToString,
                response_deserializer=onnx__pb2.ONNX.FromString,
                )
        self.UploadSolver = channel.unary_unary(
                '/Solver/UploadSolver',
                request_serializer=ipss__pb2.Service.SerializeToString,
                response_deserializer=api__pb2.Empty.FromString,
                )
        self.StreamLogs = channel.unary_stream(
                '/Solver/StreamLogs',
                request_serializer=api__pb2.Empty.SerializeToString,
                response_deserializer=api__pb2.File.FromString,
                )
        self.Solve = channel.unary_unary(
                '/Solver/Solve',
                request_serializer=api__pb2.Cnf.SerializeToString,
                response_deserializer=api__pb2.Interpretation.FromString,
                )


class SolverServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartTrain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTrain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTensor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadSolver(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Solve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SolverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartTrain': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTrain,
                    request_deserializer=api__pb2.Empty.FromString,
                    response_serializer=api__pb2.Empty.SerializeToString,
            ),
            'StopTrain': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTrain,
                    request_deserializer=api__pb2.Empty.FromString,
                    response_serializer=api__pb2.Empty.SerializeToString,
            ),
            'GetTensor': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTensor,
                    request_deserializer=api__pb2.Empty.FromString,
                    response_serializer=onnx__pb2.ONNX.SerializeToString,
            ),
            'UploadSolver': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadSolver,
                    request_deserializer=ipss__pb2.Service.FromString,
                    response_serializer=api__pb2.Empty.SerializeToString,
            ),
            'StreamLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamLogs,
                    request_deserializer=api__pb2.Empty.FromString,
                    response_serializer=api__pb2.File.SerializeToString,
            ),
            'Solve': grpc.unary_unary_rpc_method_handler(
                    servicer.Solve,
                    request_deserializer=api__pb2.Cnf.FromString,
                    response_serializer=api__pb2.Interpretation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Solver', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Solver(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartTrain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Solver/StartTrain',
            api__pb2.Empty.SerializeToString,
            api__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTrain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Solver/StopTrain',
            api__pb2.Empty.SerializeToString,
            api__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTensor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Solver/GetTensor',
            api__pb2.Empty.SerializeToString,
            onnx__pb2.ONNX.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadSolver(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Solver/UploadSolver',
            ipss__pb2.Service.SerializeToString,
            api__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Solver/StreamLogs',
            api__pb2.Empty.SerializeToString,
            api__pb2.File.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Solve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Solver/Solve',
            api__pb2.Cnf.SerializeToString,
            api__pb2.Interpretation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
