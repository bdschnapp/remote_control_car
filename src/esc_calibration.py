from gpiozero import PWMOutputDevice
import time

MOTOR_PIN = 4
motor = PWMOutputDevice(MOTOR_PIN, 50)

while True:
    val = float(input("Duty Cycle: "))
    if val == -100:
        break
    motor.value = val
    time.sleep(.5)