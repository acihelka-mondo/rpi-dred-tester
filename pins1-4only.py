import RPi.GPIO as GPIO
import time
import os

pin1 = 0
pin2 = 5
pin3 = 6
pin4 = 13
pin5 = 19
pin6 = 26

GPIO.setmode(GPIO.BCM)

# set pins1-4 as input, pull-down
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        os.system("clear") # clear text

        # check modes
        print("import dr modes:")
        if(GPIO.input(pin1) == 1):
            print("drm1")
        if(GPIO.input(pin2) == 1):
            print("drm2")
        if(GPIO.input(pin3) == 1):
            print("drm3")
        if(GPIO.input(pin4) == 1):
            print("drm4")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nApplication stopped!")
finally GPIO.cleanup()