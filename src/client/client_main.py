import numpy as np
import cv2
import grpc_auto
import grpc
import time
import lane_detection


if __name__ == '__main__':
    steering_angle = 0
    motor_speed = 0

    try:
        while True:
            start_time = time.time()
            with grpc.insecure_channel('localhost:50050') as channel:
                stub = grpc_auto.vision_pb2_grpc.VisionStub(channel)
                response = stub.capture(grpc_auto.vision_pb2.visionRequest())

            if response.success:

                np_arr = np.fromstring(response.img, np.uint8)
                img = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)

                edges = lane_detection.detect_edges(img)
                line_segments = lane_detection.detect_line_segments(edges)
                lane_lines = lane_detection.average_slope_intercept(img, line_segments)

                if len(lane_lines) > 0:

                    lane_lines_image = lane_detection.display_lines(img, lane_lines)
                    cv2.imshow("lane lines", lane_lines_image)

                    new_steering_angle = lane_detection.compute_steering_angle(img, lane_lines)
                    stabilized_steering_angle = lane_detection.stabilize_steering_angle(
                        steering_angle, new_steering_angle, len(lane_lines))

                    steering_angle = stabilized_steering_angle

                else:  # no lane lines detected
                    motor_speed = 0
                    steering_angle = 0

            else:  # no img received
                motor_speed = 0
                steering_angle = 0

            with grpc.insecure_channel('localhost:50050') as channel:
                stub = grpc_auto.control_pb2_grpc.ControlStub(channel)
                turn_response = stub.turn(grpc_auto.control_pb2.turnRequest(position=(steering_angle/90)))
                # speed_response = stub.speed(grpc_auto.control_pb2.speedRequest(speed=motor_speed))

            comp_time = time.time() - start_time
            if comp_time < 0.2:
                time.sleep(0.2 - comp_time)

    except Exception as e:
        print(str(e))





