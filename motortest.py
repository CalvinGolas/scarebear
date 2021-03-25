import RPi.GPIO as GPIO
import time

servoPIN = 26
servoTwoPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoTwoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 26 for PWM with 50 Hz
p.start(2.5) #initialization
s = GPIO.PWM(servoTwoPIN, 50)
s.start(2.5)
try:
    while True:
        p.ChangeDutyCycle(5)
        time.sleep(1)
        p.ChangeDutyCycle(10)
        time.sleep(1)
        s.ChangeDutyCycle(5)
        time.sleep(1)
        s.ChangeDutyCycle(10)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    s.stop()
    GPIO.cleanup()
