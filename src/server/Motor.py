from gpiozero import PWMOutputDevice, DigitalOutputDevice


FORWARD = 1
OFF = 0
REVERSE = -1


class DCMotor:
    def __init__(self, pwm, in_1, in_2):
        self.speed = PWMOutputDevice(pin=pwm, frequency=50)
        self.in_1 = DigitalOutputDevice(pin=in_1)
        self.in_2 = DigitalOutputDevice(pin=in_2)
        self.direction = FORWARD

    def stop(self):
        self.speed.value = 0
        self.in_1.off()
        self.in_2.off()
        self.direction = OFF

    def direction_control(self, direction=None):
        try:
            self.speed.value = 0

            if direction == None:
                self.in_1.off()
                self.in_2.off()
                self.direction = OFF
                return True

            if direction == FORWARD:
                self.in_1.on()
                self.in_2.off()
                self.direction = FORWARD
                return True

            if direction == REVERSE:
                self.in_1.off()
                self.in_2.on()
                self.direction = REVERSE
                return True

        except Exception as e:
            print(str(e))
            return False
