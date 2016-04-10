# Run this file on a Raspberry Pi with this command:
# sudo python3 LED7.py
# You will be asked for your password.
#
# If this does not work, run this command:
# sudo apt-get update && sudo apt-get install -y python-dev python-rpi.gpio

# Import the RPIO module, which connects Python with the pins of the Raspberry Pi, and the time module, which allows Python to track the passage of time
import RPi.GPIO as GPIO
import time

# Choose which GPIO pin to use
led = 7

# set up GPIO as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# set pin GPIO7 to be "on," turning on the light
GPIO.output(led, 1)

# delays for 1 second, keeping the light on briefly
time.sleep(1)

# set pin GPIO7 to be "off," turning off the light
GPIO.output(led, 0)

# delays for 1 second, keeping the light off briefly
time.sleep(1)

# set pin GPIO7 to be "on," turning on the light
GPIO.output(led, 1)

# delays for 1 second, keeping the light on briefly
time.sleep(1)

# set pin GPIO7 to be "off," turning off the light
GPIO.output(led, 0)

# delays for 1 second, keeping the light off briefly
time.sleep(1)