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

        # set pins5,6 output (import mode)
        GPIO.setup(pin5, GPIO.OUT)
        GPIO.setup(pin6, GPIO.OUT)
                
        GPIO.output(pin5, GPIO.LOW)
        GPIO.output(pin6, GPIO.HIGH)

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

        # swap pin5,6 states (export mode)
        GPIO.setup(pin5, GPIO.OUT)
        GPIO.setup(pin6, GPIO.OUT)

        GPIO.output(pin5, GPIO.HIGH)
        GPIO.output(pin6, GPIO.LOW)
        

        # check modes
        print("export dr modes:")
        if(GPIO.input(pin1) == 1):
            print("drm5")
        if(GPIO.input(pin2) == 1):
            print("drm6")
        if(GPIO.input(pin3) == 1):
            print("drm7")
        if(GPIO.input(pin4) == 1):
            print("drm8")


        # check drm0
        GPIO.setup(pin6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin6 to input
        print("other dr mode:")
        if(GPIO.input(pin6) == 1):
            print("drm0")

except KeyboardInterrupt:
    print("\nApplication stopped!")