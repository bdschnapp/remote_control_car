from gpiozero import PWMOutputDevice

from picamera.array import PiRGBArray
from picamera import PiCamera
from cv2 import imencode


import grpc
import grpc_auto  # auto generated code from proto files

import time
import threading
import subprocess
from concurrent import futures
import logging

import Motor

FORWARD = 1
OFF = 0
REVERSE = -1

SERVO_PIN = "GPIO3"  # pin 5, servo PWM signal

# if motor direction is opposite of expected, either switch IN1 and IN2 in the software, or switch the motor cables
IN1 = "GPIO17"  # pin 11, H bridge pin 1
IN2 = "GPIO27"  # pin 13, H bridge pin 2
ENA = "GPIO22"  # pin 15, motor PWM signal

servo = PWMOutputDevice(pin=SERVO_PIN, frequency=50)
dc_motor = Motor.DCMotor(ENA, IN1, IN2)

camera = PiCamera()
rawCapture = PiRGBArray(camera)

video = PiCamera()
video.resolution = (640, 480)
video.framerate = 32
rawCaptureVideo = PiRGBArray(video, size=(640, 480))

time.sleep(0.1)


class Control(grpc_auto.control_pb2_grpc.ControlServicer):

    def turn(self, request, context):
        if (request.position > 1) or (request.position < -1):
            return grpc_auto.control_pb2.turnReply(success=0)

        servo.value = (request.position + 1)
        return grpc_auto.control_pb2.turnReply(success=1)

    def speed(self, request, context):
        if (request.speed > 1) or (request.speed < -1):
            return grpc_auto.control_pb2.speedReply(success=0)

        if request.speed == 0:
            if dc_motor.direction != OFF:
                if not dc_motor.direction_control():
                    return grpc_auto.control_pb2.speedReply(success=0)
                dc_motor.speed.value = 0

        elif request.speed > 0:
            if dc_motor.direction != FORWARD:
                if not dc_motor.direction_control(FORWARD):
                    return grpc_auto.control_pb2.speedReply(success=0)
            dc_motor.speed.value = request.speed

        else:
            if dc_motor.direction != REVERSE:
                if not dc_motor.direction_control(REVERSE):
                    return grpc_auto.control_pb2.speedReply(success=0)
            dc_motor.speed.value = abs(request.speed)

        return grpc_auto.control_pb2.speedReply(success=1)


class Vision(grpc_auto.vision_pb2_grpc.VisionServicer):

    def capture(self, request, context):
        try:
            camera.capture(rawCapture, format="bgr")
            img = rawCapture.array
            img_str = imencode('.jpg', img)[1].tostring()

            return grpc_auto.vision_pb2.visionReply(img=img_str, success=1)
        except Exception as e:
            print(str(e))
            return grpc_auto.vision_pb2.visionReply(img=None, success=0)


def wifi_detection():
    # command only works on linux based OS.
    if subprocess.run(["ping", "192.168.4.1", "-c", "1", "-W", "1"], capture_output=True).returncode != 0:
        dc_motor.stop()

    threading.Timer(1.0, wifi_detection).start()


def clear_camera_data():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)


def serve():
    server_thread_pool = futures.ThreadPoolExecutor(max_workers=10)
    server = grpc.server(thread_pool=server_thread_pool, maximum_concurrent_rpcs=10)
    grpc_auto.control_pb2_grpc.add_ControlServicer_to_server(Control(), server)
    grpc_auto.vision_pb2_grpc.add_VisionServicer_to_server(Vision(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    wifi_detection()
    #server_thread_pool.submit(clear_camera_data)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
