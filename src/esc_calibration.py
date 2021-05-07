from gpiozero import PWMOutputDevice, DigitalOutputDevice
import time

IN1 = "GPIO17"  # pin 11
IN2 = "GPIO27"  # pin 13
ENA = "GPIO22"  # pin 15
motor = PWMOutputDevice(pin=ENA, frequency=50)
in_1 = DigitalOutputDevice(pin=IN1)
in_2 = DigitalOutputDevice(pin=IN2)


def direction_control(direction):
    motor.value = 0
    time.sleep(0.01)

    if direction:
        in_1.on()
        in_2.off()
    else:
        in_1.off()
        in_2.on()


while True:
    val = float(input("Duty Cycle: "))
    if val == -100:
        motor.value = 0
        in_1.off()
        in_2.off()
        break

    if val == -1:
        direction_control(0)

    if val == -2:
        direction_control(1)

    else:
        motor.value = val
        time.sleep(.5)
