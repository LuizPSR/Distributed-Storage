# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import keyvalue_pb2 as keyvalue__pb2


class KeyValueServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Insert = channel.unary_unary(
                '/keyvalue.KeyValueService/Insert',
                request_serializer=keyvalue__pb2.KeyValueRequest.SerializeToString,
                response_deserializer=keyvalue__pb2.ConfirmationResponse.FromString,
                )
        self.Consult = channel.unary_unary(
                '/keyvalue.KeyValueService/Consult',
                request_serializer=keyvalue__pb2.KeyRequest.SerializeToString,
                response_deserializer=keyvalue__pb2.ValueResponse.FromString,
                )
        self.Activate = channel.unary_unary(
                '/keyvalue.KeyValueService/Activate',
                request_serializer=keyvalue__pb2.ServiceRequest.SerializeToString,
                response_deserializer=keyvalue__pb2.ConfirmationResponse.FromString,
                )
        self.Terminate = channel.unary_unary(
                '/keyvalue.KeyValueService/Terminate',
                request_serializer=keyvalue__pb2.EmptyRequest.SerializeToString,
                response_deserializer=keyvalue__pb2.ConfirmationResponse.FromString,
                )


class KeyValueServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Consult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Activate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Terminate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=keyvalue__pb2.KeyValueRequest.FromString,
                    response_serializer=keyvalue__pb2.ConfirmationResponse.SerializeToString,
            ),
            'Consult': grpc.unary_unary_rpc_method_handler(
                    servicer.Consult,
                    request_deserializer=keyvalue__pb2.KeyRequest.FromString,
                    response_serializer=keyvalue__pb2.ValueResponse.SerializeToString,
            ),
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=keyvalue__pb2.ServiceRequest.FromString,
                    response_serializer=keyvalue__pb2.ConfirmationResponse.SerializeToString,
            ),
            'Terminate': grpc.unary_unary_rpc_method_handler(
                    servicer.Terminate,
                    request_deserializer=keyvalue__pb2.EmptyRequest.FromString,
                    response_serializer=keyvalue__pb2.ConfirmationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'keyvalue.KeyValueService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeyValueService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyvalue.KeyValueService/Insert',
            keyvalue__pb2.KeyValueRequest.SerializeToString,
            keyvalue__pb2.ConfirmationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Consult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyvalue.KeyValueService/Consult',
            keyvalue__pb2.KeyRequest.SerializeToString,
            keyvalue__pb2.ValueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Activate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyvalue.KeyValueService/Activate',
            keyvalue__pb2.ServiceRequest.SerializeToString,
            keyvalue__pb2.ConfirmationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Terminate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyvalue.KeyValueService/Terminate',
            keyvalue__pb2.EmptyRequest.SerializeToString,
            keyvalue__pb2.ConfirmationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
