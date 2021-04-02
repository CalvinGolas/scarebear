import RPi.GPIO as GPIO
import time

#This will be used to define predertemined actions the bear motors will take and simplify theme so that making new stories is easier
class BearControl:

    #calculates what signal needs to be sent to the servo and specifies angle
    def get_angle(self, degree):
        return degree / 18.0 + 2

    def turn_head_backwards(self):
       self.neckServoPin.ChangeDutyCycle(self.get_angle(180)) 

    def straighten_head(self):
        self.neckServoPin.ChangeDutyCycle(self.get_angle(90))

    def turn_head_specific(self, degree):
        self.neckServoPin.ChangeDutyCycle(self.get_angle(degree))

    def vibrate_head(self):
        self.neckServoPin.ChangeDutyCycle(self.get_angle(45))
        time.sleep(.5)
        self.neckServoPin.ChangeDutyCycle(self.get_angle(135))
        time.sleep(.5)
        self.neckServoPin.ChangeDutyCycle(self.get_angle(80))
        time.sleep(.5)
        self.neckServoPin.ChangeDutyCycle(self.get_angle(165))
        time.sleep(.5)


    def lower_fangs(self):
        self.mouthServoPin.ChangeDutyCycle(4.7)
        time.sleep(.5)
        self.mouthServoPin.ChangeDutyCycle(0)

    def raise_fangs(self):
        self.mouthServoPin.ChangeDutyCycle(3.5)
        time.sleep(.5)
        self.mouthServoPin.ChangeDutyCycle(0)


    # halts the bear parts and cleans up any messes that may have been created
    def halt(self):
        self.mouthServoPin.stop()
        self.neckServoPin.stop()
        GPIO.cleanup()

    # initializes and sets up bear parts based on provided GPIO pins
    def __init__(self, mouthServoPin, neckServoPin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(mouthServoPin, GPIO.OUT)
        GPIO.setup(neckServoPin, GPIO.OUT)
        self.mouthServoPin = GPIO.PWM(mouthServoPin, 50)
        self.neckServoPin = GPIO.PWM(neckServoPin, 50)
        self.mouthServoPin.start(2.5)
        self.neckServoPin.start(2.5)
