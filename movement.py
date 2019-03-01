import RPi.GPIO as GPIO
import time

print("Start")

## Set to name the pins by position

GPIO.setmode(GPIO.BOARD)

## Create the Output Channels for Right Motor

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

## Create the Enable Channel for Right Motor

GPIO.setup(12, GPIO.OUT)

## Create the Output Channels for Left Motor

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

## Create the Enable Channel for Left Motor

GPIO.setup(33, GPIO.OUT)

## Create PWM for Left and Right Motors
# GPIO.PWM(pin, frequency)

pwmLeft = GPIO.PWM(33, 100)
pwmRight = GPIO.PWM(12, 100)

## Create Functions to go Forwards 

def forward():
    try:
        while True:
            pwmLeft.start(0)
            pwmRight.start(0)
            print("Forward")
            # Right Motor
            GPIO.output(16, True)
            GPIO.output(18, False)
            GPIO.output(12, True)
            # Left Motor
            GPIO.output(13, False)
            GPIO.output(15, True)
            GPIO.output(33, True)
            # Change Duty Cycle
            pwmLeft.ChangeDutyCycle(100)
            pwmRight.ChangeDutyCycle(100)
            time.sleep(.5)
    except KeyboardInterrupt:
        pass
    pwmLeft.stop()
    pwmRight.stop()
    GPIO.output(12, False)
    GPIO.output(33, False)
    print("Stop")

def backward():
    try:
        while True:
            pwmLeft.start(0)
            pwmRight.start(0)
            print("Backward")
            # Right Motor
            GPIO.output(16, False)
            GPIO.output(18, True)
            GPIO.output(12, True)
            # Left Motor
            GPIO.output(13, True)
            GPIO.output(15, False)
            GPIO.output(33, True)
            # Change Duty Cycle
            pwmLeft.ChangeDutyCycle(100)
            pwmRight.ChangeDutyCycle(100)
            time.sleep(.5)
    except KeyboardInterrupt:
        pass
    pwmLeft.stop()
    pwmRight.stop()
    GPIO.output(12, False)
    GPIO.output(33, False)
    print("Stop")

forward()
backward()
GPIO.cleanup()
print('Clean')
