from gpiozero import PWMOutputDevice

import grpc
import grpc_auto  # auto generated code from proto files

from concurrent import futures
import logging

SERVO_PIN = 3
MOTOR_PIN = 17

servo = PWMOutputDevice(SERVO_PIN, frequency=50)
motor = PWMOutputDevice(MOTOR_PIN, frequency=50)


class Control(grpc_auto.control_pb2_grpc.ControlServicer):

    def turn(self, request, context):
        servo.value = ((request.position / 2) + 1)
        return grpc_auto.control_pb2.turnReply(success=1)

    def speed(self, request, context):
        motor.value = ((request.position / 2) + 2)
        return grpc_auto.control_pb2.speedReply(success=1)


class Vision(grpc_auto.vision_pb2_grpc.VisionServicer):

    def capture(self, request, context):
        image = 0
        return grpc_auto.vision_pb2.visionReply(img=image, success=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_auto.control_pb2_grpc.add_ControlServicer_to_server(Control(), server)
    grpc_auto.vision_pb2_grpc.add_VisionServicer_to_server(Vision(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
