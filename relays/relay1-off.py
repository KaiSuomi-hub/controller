import RPi.GPIO as GPIO
import time
#gpio out nr 4 = channel 14
channel = 4

# GPIO setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor off


def motor_on(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor on


if __name__ == '__main__':
    try:
        motor_off(channel)
        sleep(
            1000
        )
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()