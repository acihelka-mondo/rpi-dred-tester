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
#os.system("pinctrl 0,5,6,13 pd ip")

# GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#os.system("clear") # clear text

# GPIO.setup(pin6, GPIO.OUT)
# GPIO.output(pin6, GPIO.HIGH)

GPIO.setup(pin6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin1, GPIO.OUT)
GPIO.output(pin1, GPIO.HIGH)

# check modes
print("import dr modes:")
if(GPIO.input(pin6) == 1):
    print("drm1")
# if(GPIO.input(pin2) == 1):
#     print("drm2")
# if(GPIO.input(pin3) == 1):
#     print("drm3")
# if(GPIO.input(pin4) == 1):
#     print("drm4")

#os.system('pinctrl | grep -e "GPIO0 " -e "GPIO5 " -e "GPIO6 " -e "GPIO13 " -e "GPIO19 " -e "GPIO26 "')
GPIO.cleanup()
# os.system('pinctrl | grep -e "GPIO0 " -e "GPIO5 " -e "GPIO6 " -e "GPIO13 " -e "GPIO19 " -e "GPIO26 "')

