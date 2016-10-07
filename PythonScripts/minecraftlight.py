# While Minecraft: Pi Edition is running, run this file on a Raspberry Pi with this command:
# python minecrafthack.sh

# import the modules
from mcpi import block
from mcpi import minecraft
import RPi.GPIO as GPIO
import time

# First make a connection between python and the game
mc = minecraft.Minecraft.create()

# set up GPIO7 as an output
led = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# mc is a object we can call to control the world.  Let's say, "Hello!"
mc.postToChat("MrMike spells MIKE and lights up a light!")

# Turn GPIO7 on
GPIO.output(led, 1)

# Delay for 1 second, keeping the light on briefly
time.sleep(1)

# Turn GPIO7 off
GPIO.output(led, 0)

# delay for 1 second, keeping the light off briefly
time.sleep(1)

# You could read the coordinates in the top left, and choose numbers near those.

# Try to spell a word in the sky.  It is very easy with copy and paste. I will write my name in the sky.
# M
mc.setBlock(5, 14, 5, block.GOLD_BLOCK)
mc.setBlock(5, 13, 5, block.GOLD_BLOCK)
mc.setBlock(5, 12, 5, block.GOLD_BLOCK)
mc.setBlock(5, 11, 5, block.GOLD_BLOCK)
mc.setBlock(5, 10, 5, block.GOLD_BLOCK)
mc.setBlock(5, 13, 6, block.GOLD_BLOCK)
mc.setBlock(5, 12, 7, block.GOLD_BLOCK)
mc.setBlock(5, 13, 8, block.GOLD_BLOCK)
mc.setBlock(5, 14, 9, block.GOLD_BLOCK)
mc.setBlock(5, 13, 9, block.GOLD_BLOCK)
mc.setBlock(5, 12, 9, block.GOLD_BLOCK)
mc.setBlock(5, 11, 9, block.GOLD_BLOCK)
mc.setBlock(5, 10, 9, block.GOLD_BLOCK)

# I spelled the letter M.  Try to write your name and impress your friends!

# Turn GPIO7 on
GPIO.output(led, 1)

# Delay for 1 second, keeping the light on briefly
time.sleep(1)

# Turn GPIO7 off
GPIO.output(led, 0)

# delay for 1 second, keeping the light off briefly
time.sleep(1)

# I
mc.setBlock(5, 10, 11, block.GOLD_BLOCK)
mc.setBlock(5, 11, 11, block.GOLD_BLOCK)
mc.setBlock(5, 12, 11, block.GOLD_BLOCK)
mc.setBlock(5, 13, 11, block.GOLD_BLOCK)
mc.setBlock(5, 14, 11, block.GOLD_BLOCK)

# Turn GPIO7 on
GPIO.output(led, 1)

# Delay for 1 second, keeping the light on briefly
time.sleep(1)

# Turn GPIO7 off
GPIO.output(led, 0)

# delay for 1 second, keeping the light off briefly
time.sleep(1)

# K
mc.setBlock(5, 14, 13, block.GOLD_BLOCK)
mc.setBlock(5, 13, 13, block.GOLD_BLOCK)
mc.setBlock(5, 12, 13, block.GOLD_BLOCK)
mc.setBlock(5, 11, 13, block.GOLD_BLOCK)
mc.setBlock(5, 10, 13, block.GOLD_BLOCK)
mc.setBlock(5, 12, 14, block.GOLD_BLOCK)
mc.setBlock(5, 11, 15, block.GOLD_BLOCK)
mc.setBlock(5, 13, 15, block.GOLD_BLOCK)
mc.setBlock(5, 10, 16, block.GOLD_BLOCK)
mc.setBlock(5, 14, 16, block.GOLD_BLOCK)

# Turn GPIO7 on
GPIO.output(led, 1)

# Delay for 1 second, keeping the light on briefly
time.sleep(1)

# Turn GPIO7 off
GPIO.output(led, 0)

# delay for 1 second, keeping the light off briefly
time.sleep(1)

# E
mc.setBlock(5, 14, 18, block.GOLD_BLOCK)
mc.setBlock(5, 13, 18, block.GOLD_BLOCK)
mc.setBlock(5, 12, 18, block.GOLD_BLOCK)
mc.setBlock(5, 11, 18, block.GOLD_BLOCK)
mc.setBlock(5, 10, 18, block.GOLD_BLOCK)
mc.setBlock(5, 10, 19, block.GOLD_BLOCK)
mc.setBlock(5, 14, 19, block.GOLD_BLOCK)
mc.setBlock(5, 12, 19, block.GOLD_BLOCK)
mc.setBlock(5, 10, 20, block.GOLD_BLOCK)
mc.setBlock(5, 14, 20, block.GOLD_BLOCK)

# Turn GPIO7 on
GPIO.output(led, 1)

# Delay for 1 second, keeping the light on briefly
time.sleep(1)

# Turn GPIO7 off
GPIO.output(led, 0)

# delay for 1 second, keeping the light off briefly
time.sleep(1)

# Water
mc.setBlock(5, 10, 23, block.WATER)


# Turn GPIO7 on
GPIO.output(led, 1)

# Delay for 1 second, keeping the light on briefly
time.sleep(1)

# Turn GPIO7 off
GPIO.output(led, 0)
