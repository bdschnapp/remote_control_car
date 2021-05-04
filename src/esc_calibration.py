from gpiozero import PWMOutputDevice
import time

MOTOR_PIN = "GPIO4"
motor = PWMOutputDevice(pin=MOTOR_PIN, frequency=50)

while True:
    val = float(input("Duty Cycle: "))
    if val == -100:
        break
    motor.value = val
    time.sleep(.5)