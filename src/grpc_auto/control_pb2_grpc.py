# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import control_pb2 as control__pb2


class ControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turn = channel.unary_unary(
                '/control.Control/turn',
                request_serializer=control__pb2.turnRequest.SerializeToString,
                response_deserializer=control__pb2.turnReply.FromString,
                )
        self.speed = channel.unary_unary(
                '/control.Control/speed',
                request_serializer=control__pb2.speedRequest.SerializeToString,
                response_deserializer=control__pb2.speedReply.FromString,
                )


class ControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def turn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def speed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turn': grpc.unary_unary_rpc_method_handler(
                    servicer.turn,
                    request_deserializer=control__pb2.turnRequest.FromString,
                    response_serializer=control__pb2.turnReply.SerializeToString,
            ),
            'speed': grpc.unary_unary_rpc_method_handler(
                    servicer.speed,
                    request_deserializer=control__pb2.speedRequest.FromString,
                    response_serializer=control__pb2.speedReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'control.Control', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Control(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def turn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/control.Control/turn',
            control__pb2.turnRequest.SerializeToString,
            control__pb2.turnReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def speed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/control.Control/speed',
            control__pb2.speedRequest.SerializeToString,
            control__pb2.speedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
