# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2


class RandomStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RandomCnf = channel.unary_unary(
                '/api.Random/RandomCnf',
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
            'api.Random', rpc_method_handlers)
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
        return grpc.experimental.unary_unary(request, target, '/api.Random/RandomCnf',
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
        self.StartTrain = channel.stream_stream(
                '/api.Solver/StartTrain',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.StopTrain = channel.stream_stream(
                '/api.Solver/StopTrain',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.GetTensor = channel.stream_stream(
                '/api.Solver/GetTensor',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.UploadSolver = channel.stream_stream(
                '/api.Solver/UploadSolver',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.StreamLogs = channel.stream_stream(
                '/api.Solver/StreamLogs',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.Solve = channel.stream_stream(
                '/api.Solver/Solve',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.AddTensor = channel.stream_stream(
                '/api.Solver/AddTensor',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.GetDataSet = channel.stream_stream(
                '/api.Solver/GetDataSet',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )
        self.AddDataSet = channel.stream_stream(
                '/api.Solver/AddDataSet',
                request_serializer=api__pb2.Buffer.SerializeToString,
                response_deserializer=api__pb2.Buffer.FromString,
                )


class SolverServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartTrain(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTrain(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTensor(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadSolver(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamLogs(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Solve(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTensor(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataSet(self, request_iterator, context):
        """Hasta que se implemente AddTensor.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddDataSet(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SolverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartTrain': grpc.stream_stream_rpc_method_handler(
                    servicer.StartTrain,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'StopTrain': grpc.stream_stream_rpc_method_handler(
                    servicer.StopTrain,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'GetTensor': grpc.stream_stream_rpc_method_handler(
                    servicer.GetTensor,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'UploadSolver': grpc.stream_stream_rpc_method_handler(
                    servicer.UploadSolver,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'StreamLogs': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamLogs,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'Solve': grpc.stream_stream_rpc_method_handler(
                    servicer.Solve,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'AddTensor': grpc.stream_stream_rpc_method_handler(
                    servicer.AddTensor,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'GetDataSet': grpc.stream_stream_rpc_method_handler(
                    servicer.GetDataSet,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
            'AddDataSet': grpc.stream_stream_rpc_method_handler(
                    servicer.AddDataSet,
                    request_deserializer=api__pb2.Buffer.FromString,
                    response_serializer=api__pb2.Buffer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.Solver', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Solver(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartTrain(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/StartTrain',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTrain(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/StopTrain',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTensor(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/GetTensor',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadSolver(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/UploadSolver',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamLogs(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/StreamLogs',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Solve(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/Solve',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTensor(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/AddTensor',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDataSet(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/GetDataSet',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddDataSet(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.Solver/AddDataSet',
            api__pb2.Buffer.SerializeToString,
            api__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
