# [Raspberry Pi Programming Workshop](#raspberrypiprogrammingworkshop)

RPiPW = resources + notes + code samples for a workshop introducing the
Raspberry Pi as a beginner's programming environment

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br>
Copyright © Michael McMahon 2015-2018.  Except where otherwise specified, the
text on
[Raspberry Pi Programming Workshop](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/)
by Michael McMahon is licensed under the
[Creative Commons Attribution-ShareAlike License 4.0 (International) (CC-BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).


## Table of Contents

- [The Raspberry Pi](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#the-raspberry-pi) 
  - [Purchasing a Raspberry Pi](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#purchasing-a-raspberry-pi) 
  - [Operating Systems for the Raspberry Pi](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#operating-systems-for-the-raspberry-pi) 
  - [Installing Raspbian via NOOBS](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#installing-raspbian-via-noobs) 
  - [Software Repositories](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#software-repositories) 
- [Introduction to Programming](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#introduction-to-programming) 
  - [Hello, world!](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#hello-world) 
  - [Infinite Loops](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#infinite-loops) 
  - [GPIO: General Purpose Input/Output](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#gpio) 
  - [Python and pygame](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#python-and-pygame) 
  - [Photo Editing](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#photo-editing) 
  - [Minecraft: Pi Edition](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#minecraft-pi-edition) 
  - [Looping GPIO with Minecraft](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#looping-gpio-with-minecraft) 
  - [Processing](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#processing) 
  - [Computer Vision: opencv-python and SimpleCV](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#computer-vision-opencv-python-and-simplecv) 
- [Taking The Raspberry Pi Further](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#taking-the-raspberry-pi-further) 
  - [Projects](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#projects) 
  - [Problems and Solutions That Worked for Me](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#problems-and-solutions-that-worked-for-me) 
  - [Raspberry Pi Giveaway](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#raspberry-pi-giveaway) 
  - [Resources](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#resources)




## The Raspberry Pi
<!-- Separate this section into more sections: buying and connecting -->

The Raspberry Pi is a low-cost, low-power single board computer the size of a
credit card.  With a low price point and advanced software, it is a great tool
to teach youth electronics and programming.

The Pi is developed by the Raspberry Pi Foundation.  Their goal is ''to advance
the education of adults and children, particularly in the field of computers,
computer science and related subjects,'' according to their
[about us page](https://www.raspberrypi.org/about/).

Children buy $60 video games for expensive consoles each year.  What if they
purchased a computer with that money instead?  They could take the same HDMI
cable out of their video game system and plug it into a Raspberry Pi.

<img src="https://www.element14.com/community/servlet/JiveServlet/showImage/102-80899-13-252356/Pi3+Breakout+Feb+29+2016.png"/>

Breakdown of various available models of the Raspberry Pi

Release Date | Original Price | Model | GPIO Pins | CPU
------| ----- | ----- |-----------|---------
Mar 2018 | $35 | 3 B+ | 40 | 1.4 GHz ARMv8 64 bit (quad core)
Jan 2018 | $10 | Zero WH | 40 | 1.0GHz ARMv6 (single core)
Feb 2017 | $10 | Zero W | 40 | 1.0GHz ARMv6 (single core)
Feb 2016 | $35 | 3 B | 40 | 1.2GHz ARMv8 64bit (quad core)
Nov 2015 | $5 | Zero | 40 | 1.0GHz ARMv6 (single core)
Feb 2015 | $35 | 2 B | 40 | 900MHz ARMv7 (quad core)
Nov 2014 | $20 | 1 A+ | 40 | 700MHz ARMv6 (single core)
July 2014 | $25 | 1 B+ | 40 | 700MHz ARMv6 (single core)
Apr 2014 | $30 | Compute | 200 | 700MHz ARMv6 (single core)
Feb 2012 | $25 | 1 A | 26 | 700MHz ARMv6 (single core)
Feb 2012 | $35 | 1 B | 26 | 700MHz ARMv6 (single core)

There are other SBCs (Single Board Computers) available.  The Raspberry Pi is
not the best, but the Raspberry Pi is one of the cheapest and most popular
boards.  Other SBCs include
[OEMA68](https://www.crowdsupply.com/eoma68/micro-desktop),
[Parallella with 18 core processors](http://www.parallella.org/board/),
[OLinuXino](https://www.olimex.com/Products/OlinuXino/),
[Banana Pi](http://www.lemaker.org/),
[C.H.I.P. the $9 base modular computer](http://nextthing.co/),
[Beagleboards](http://beagleboard.org/), and
[Cubieboards](http://cubieboard.org/).  With anything popular in the open source
community, higher numbers of people working on a projects yields more projects,
tutorials, and development.  I started with the journey into single board
computers with the Raspberry Pi model 1 B.

Electricity efficiency: A typical desktop computer without a monitor consumes
200 W 800 mA.  If you were to leave a full computer running all day for a year,
you would be using 1752 kilowatt-hours or about $630 on your electric bill.  A 5
W Raspberry Pi running all day for a year would use 43.8 kilowatt-hours or about
$15.  This makes a large environmental difference for long-term projects like
hosting a web server or opening your garage when your phone comes within range.
[source](http://michaelbluejay.com/electricity/computers.html)




## Purchasing a Raspberry Pi

What about all of the extra things you need to make it work?  I made a shopping
cart at the Cambridge, MA Micro Center page with everything I would buy for one.

- $29.99 RS Raspberry Pi 3 Model B
-  $8.99 Micro-USB Power Supply 5 volt 2.5 amp
-  $3.99 Inland Wired Optical Mouse
-  $3.99 Inland Wired Keyboard
-  $5.99 Micro Center 16GB micro SDHC Class 10 Flash Media Card

- $52.95 Subtotal
-  $4.50 Tax
- $57.45 Grand Total

Some of these items are commonly lying around already.  Cheaper prices can be
found at other online stores, thrift stores, and garage sales.  Three things
that I did not include are a case, and HDMI cable, and a screen with HDMI or
DVI.  Optionally, Legos or a
[3D printer](http://www.thingiverse.com/search?q=raspberry+pi&sa=) can be used
to build a case.  TVs are almost everywhere.

Another ready to go option is
[the pi-top for $300 or the pi-topCEED for $150](https://www.pi-top.com/) which
are Raspberry Pi workstations that include monitors.




## Operating Systems for the Raspberry Pi

There are many different operating systems available for the Raspberry Pi.  My
personal favorite is
[Arch for Arm](http://archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2)
as it is the fastest operating system for the Pi that I am aware of.  For this
tutorial, I will use Raspbian because it contains software to get started, has
excellent community support, and most project tutorials use Raspbian as a
starting point.
<br><br>
Why GNU/Linux?  GNU/Linux is built on
[free and open source software](https://en.wikipedia.org/wiki/Free_and_open_source_software)
and can be easily downloaded, modified, distributed, and used with few to no
restrictions.  This is very beneficial for a programming environment.  GNU/Linux
is also used by the most advanced science and technology institutions such as
the International Space Station, CERN, US Navy, US DOD, FAA, USPS, Google,
Novell, IBM, Cisco, and Amazon.
<br>
Other operating systems to note are
[pi-topOS](https://www.pi-top.com/product/pi-top-os),
[Fedberry](http://fedberry.org/),
[OpenWRT](http://wiki.openwrt.org/toh/raspberry_pi_foundation/raspberry_pi),
[RISC OS](https://www.riscosopen.org/content/downloads/raspberry-pi),
[OSMC](https://osmc.tv/),
[FreeBSD](https://wiki.freebsd.org/FreeBSD/arm/Raspberry%20Pi), and many more.
You can even make your own operating system for the Raspberry Pi.




## Installing Raspbian via NOOBS

The Raspberry Pi usually does not come with an operating system or storage.  You
run the operating system from a microSD.  If you have never installed or
experimented with GNU/Linux before, use NOOBS.  It was made to be as easy as
possible.  If you mess it up, hold shift while you boot and reinstall.

[Video tutorial of installing NOOBS](https://www.raspberrypi.org/help/noobs-setup/)

1. Download this large zip file to your other computer:
   https://downloads.raspberrypi.org/NOOBS_latest
2. You will need a class 10 microSD card greater than or equal to 8GB.  If you
   have other files on the microSD card you will be using, back those up to
   another location, then
   [format the microSD card to FAT32](https://www.raspberrypi.org/documentation/installation/sdxc_formatting.md).
   Extract all of the files directly to a microSD card.
3. Put the microSD card into the Raspberry Pi and plug in your power supply.
   The Raspberry Pi will light up.
4. A menu of operating systems appears.  Put a check next to Raspbian.  At the
   bottom of the screen change the international options to your country.  I
   choose US.  There are many differences between a keyboard in the United
   States and one in Great Britain.  Click ''Install'' and wait a long while.
5. You have an Operating System!

If copying files to a microSD card is too daunting of a task, preinstalled cards
are also available for purchase.




## Software Repositories

Every GNU/Linux distribution has a set of software that can be installed for
free called a repository.  The App Store and Google Play store were based on the
concept of a repository.  All of your software can be installed and updated from
one central place.  To get a visual glipse of the repository, I like to use a
program called ''synaptic''.

IMPORTANT: To open a terminal in Raspbian, click on the black rectangle in the
upper left of the screen.<br>
To install synaptic, run this command in a terminal:

```
sudo apt-get install -y synaptic
```

Relevant XKCD:<br>
<a href="https://xkcd.com/149/"><img src="https://imgs.xkcd.com/comics/sandwich.png"/></a>

Open synaptic, click the update button to get the latest list of programs, and
then page down to browse.  That is an incredibly large list of programs.  All of
them are absolutely free.  Most of them are open source.  The search button at
the top right allows you to search for keywords in the name and description.




## Introduction to Programming

I would love to teach everyone to program in a day.  That is not possible.  I
can show you some cool things you can do with programming.  I can tell you how
to learn more.  You will have to do more on your own, practice, find a project
that you can work on during your spare time, search for solutions, read code and
tutorials, communicate with other programmers, ask questions, and have fun
making new things.

Why should you use the Raspberry Pi for programming?  I see lots of web
developers use these shiny, expensive laptops.  They design engaging interactive
websites.  They put them out on the Internet and then the result does not work
for the majority of computers.  They write it off and say, "Oh, well.  It works
for me."  That attitude does not change the situation they face.  Many people
cannot use their website.  Had they developed on a low spec Raspberry Pi, the
result should work on any computer or phone.

I will be using Python for these examples.  Python is an easy-to-read, beginner
programming language that can do almost anything with extra libraries.
Libraries expand the functionality of a language by adding more functions, APIs
(application program interfaces), and features.

NOTE: While learning, try to debug and follow all errors.  The error should give
line numbers.  Check that line, if it leads to another function, check that
function.  Google the error if that does not help.  Replace the file with the
original if all else fails.

I will be using many terminal commands.  It is dangerous to take the word of a
stranger on the Internet when dealing with terminal commands.  GNU/Linux has
some built in documentation.  You will need the Internet to find most
information and tutorials, but the built-in documentationation helps as a quick
reference.  You can use the ''man'' command to look up information about a
command.  To find information on using the ''ls'' command, try this in a
terminal:

```
man ls
```

You can also read the manual for the manual with this command:

```
man man
```

Python has even more built in documentation than its man page.  Open the
interactive Python prompt with this command:

```
python
```

Now we can access the interactive help menu with this command:

```
help()
```

Quit the interactive help menu with this command:

```
quit
```

Quit interactive Python with this function:

```
quit()
```

You can teach yourself the basics of using the command line with an interactive
website at:

https://www.codecademy.com/learn/learn-the-command-line

You can teach yourself the basics of Python with an interactive website at:

http://www.codecademy.com/tracks/python

I highly recommend the codecademy free resources after this workshop.  Spend at
least 15 minutes each day on codecademy when teaching yourself a new programming
language.  Codecademy is the easiest way to learn the syntax of a programming
language.  You can log in to save your progress using Facebook, Google, or make
a new account.  That is how I started learning Python.  When I thought I was
familiar enough with the Python syntax to make my own programs, I used google,
stackoverflow.com, and other websites to make new programs of my own.

It is about a 13 hour course, but doing 2-4 hours will be enough to get you
familiar with the basics of the language and the syntax.  You can use google-fu
and extra modules to script more after a few hours on codecademy.



## Hello, world!

Hello, world! is traditionally the first program that anyone writes when
tackling a new programming language.  It is a simple program that says, "Hello,"
to the world.

Relevant XKCD:<br>
<a href="https://xkcd.com/353/"><img src="https://imgs.xkcd.com/comics/python.png"/></a>

NOTICE:  This comic is dated and uses the old way to use print.  Older versions
of Python 2 used this format.  Later versions of Python 2 use the new way as
well as the old way.  It is good to be aware of this, as many old examples still
 exist on the Internet.

In a terminal, type this command:

```
python
```

The cursor will now follow three greater than symbols >>>.  Type this command
and we will be on our way:

```
print("Hello, world!")
```

If you read ''Hello, world!'' back from the computer, you succeeded.  Pat
yourself on the back and feel good about writing your first line of Python code.
Quit interactive Python with this function:

```
quit()
```

We will do this same exercise in a different way.  Open up a text editor from
the terminal using the following command line.  Leafpad and nano come installed
with Raspbian.  Nano is a terminal application so we will use that.  We will
also create a new file and give it a filename as we open it.

```
nano hello.py
```

Write out the print function again.

```
print("Hello, world!")
```

Exit by holding CTRL and pressing X.  It asks if you want to save changes.
Press Y and enter. You have now saved your program as a text file.

We will call this new text file into Python with this quick command:

```
python hello.py
```

You wrote your first program!  Now, we will get to the good stuff.

[hello.py code](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/PythonScripts/hello.py)




## Infinite Loops

I believe that infinite loops are one of the most exciting concepts in computer
science.  A ''normal'' programming book will hold out on this information until
much later.  I like to give away some spoilers.

We can copy our hello.py file from earlier to a new file with this command:

```
cp hello.py helloloop.py
```

We can open the new file with nano using this command:

```
nano helloloop.py
```

Now, add a new line to the beginning of the file that reads:

```
while True:
```

Put a tab in front of our earlier work so that the file looks like this:

```
while True:
	print("Hello, world!")
```

Exit by holding CTRL and pressing X.  It asks if you want to save changes.
Press Y and enter. You have now saved your program as a text file.

When we run this file, it will not stop printing ''Hello, world!'' until we
force the program to close.  To close the program, hold CTRL and press C.  You
could also close the terminal window, but we will need it again in a second.
Run the new program with this command:

```
python helloloop.py
```

Remember to close it by holding CTRL and pressing C once you have had enough!
That was your first loop!  Loops are great for when you want to repeat something
without having to start it each time.  Our loop is much easier to write than the
alternative:

```
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
print("Hello, world!")
```

Programming may seem like a lot of typing at first, but it allows you to type
less in the long run.

[helloloop.py code](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/PythonScripts/helloloop.py)




## GPIO: General Purpose Input/Output

If you have ever used an Arduino, you are already familiar with input/output
pins.  These can be programmed and linked to other components to build custom
circuits.  The Pi A & B have 26 pins.  The Pi A+, B+, 2 B, Zero, and 3 B have 40
pins.  The Pi Compute Module has 200 pins.


Models A & B | Models A+, B+, 2 B, Zero, and 3 B
------- | -------
<img src="http://elinux.org/images/8/80/Pi-GPIO-header-26-sm.png"/> | <img src="http://elinux.org/images/5/5c/Pi-GPIO-header.png"/>

These are programmable with Python.  I will do a simple demonstration of this
and continue onward.  If circuitry and robotics is a passion of yours, dig in.

I will use two wires and an LED light with two pins, one short and one long.
The Pi's third pin from the corner is a GROUND.  One wire will connect the LED's
short pin to the Pi's GROUND. The other wire will connect the long pin to the
pin labeled GPIO7 in the diagram above (the thirteenth pin down on the right).

We will light up the bulb using two methods:  once with Python and once with
bash.  Bash is a command line shell.  Getting to know bash is a great way for
students to start digging into the most basic elements of programming, so I
wanted to introduce it a little bit here.

Setup the modules you will need by running the following on the command line.
Modules for Python expand the functionality of the programming language.  Some
modules are associated with Python by default and many others are available to
download.  All of your modules can be listed with the Python function
''help('modules')'' from within interactive Python.  In this example, we will
use the RPIO module, which connects Python with the pins of the Pi, and the time
module, which allows Python to track the passage of time.

```
sudo apt-get update

sudo apt-get install -y python-dev python-rpi.gpio
```

We will write a Python script using nano again.  We will call the file LED7.

```
nano LED7.py
```

Once RPIO is installed, this module can be pulled into any Python script with
``import`` as shown here.

```
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
```

Exit by holding CTRL and pressing X.  It asks if you want to save changes.
Press Y and enter. You have now saved your program as a text file.

Since Python is controlling hardware with this script, it will need root
privileges.  Use this command to run the script:

```
sudo python3 LED7.py
```

The light should turn on and off.

Another way to approach this is to use bash.  Bash is the default shell for the
command line.  This is possible because everything in the system is treated like
a file, including hardware (like the pins) or other devices.  This usage of bash
is more complex than the RPIO method in pythod, but it is also very precise. We
will not focus on the code here, just be aware that it can be done if students
want to manipulate any of the hardware from the command line.

```
sudo echo "7" > /sys/class/gpio/export

sudo echo "out" > /sys/class/gpio/gpio7/direction

sudo echo "1" > /sys/class/gpio/gpio7/value

sudo echo "0" > /sys/class/gpio/gpio7/value
```

Echo is a self-explanatory command.  It repeats back what you give it.  The
greater than symbol ''>'' sends the output of the previous command to overwrite
a file.  In this case, the file is actually hardware instead of a document.
This is a unique aspect to Unix and GNU/Linux.

If you replace the LED with a motor, the same code can control a robot!

[LED7.py code](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/GPIOscripts/LED7.py)

[LED7withbash.sh code](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/GPIOscripts/LED7withbash.sh)

For more information about projects using the Raspberry Pi's GPIO, check out these links:

- https://www.raspberrypi.org/learning/python-quick-reaction-game/worksheet/
- https://pythonhosted.org/RPIO/
- https://pypi.python.org/pypi/RPi.GPIO
- http://elinux.org/RPi_Tutorial_Easy_GPIO_Hardware_%26_Software
- http://log.liminastudio.com/writing/tutorials/tutorial-how-to-use-your-raspberry-pi-like-an-arduino




# Python and pygame

Raspbian comes bundled with some games written in Python.  I like to use these
games as a starting point when teaching kids about programming in Python.  The
programs are small enough that you can read them in one sitting, and they are
very well commented.  Comments are lines that start with ''#'' and are ignored
by the computer.

We will pick a game, demonstrate how it works, read code, make a change, and
test. This is a great exercise to do with students. However, changing variables
is a backwards way to learn a language.  Remember to visit
[codecademy](http://www.codecademy.com/tracks/python) to learn more.

Pygame is a module that can be used to write games and modify them. Python, the
pygame module, and games written with pygame can be installed on GNU/Linux, Mac,
and Windows.  You do not need a Raspberry Pi for this section.

I would suggest downloading Python version 2.7 to maximize compatibility with
pygame.

- GNU/Linux Installation Instructions

Python is probably already installed on your GNU/Linux system.  You can check
that Python 2.7 is installed by running this command:

```
python -V
```

Pygame is installed by default on Raspbian.  If you are on a debian based
system, you can install pygame with this command:

```
sudo apt-get update && sudo apt-get install -y python-pygame
```

Since pygame depends on Python, the correct version of Python would also be
installed with this command.

- Mac Installation Instructions

Download
[Python](https://www.python.org/ftp/python/2.7.10/python-2.7.10-macosx10.5.pkg)
and
[pygame](http://pygame.org/ftp/pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg).
Install Python and then install pygame.  Note: I am purposefully linking to an
older release of Python 2.7.

- Windows Installation Instructions

The easiest way to install Python (and many other common programs) for Windows
is through [ninite.  Ninite](https://ninite.com/python/) is a website that
allows you to install many programs at once.  The ninite download program can be
left on your system and used as an updater in the future.

We also need the
[pygame module](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi).  Install
Python and then install pygame.

<br>

You can download the code we will start with from:

http://inventwithpython.com/makinggames_src.zip

<br>

These games written with pygame originated from the
[Invent with Python website](http://inventwithpython.com).  You can get a
[free book that accompanies the games](http://inventwithpython.com/makinggames.pdf).

There are hundreds of free games that you can modify from
[the pygame webpage](www.pygame.org">the pygame webpage).

Check out the [pygame tutorials](www.pygame.org/wiki/tutorials) for more
information.

Beginner:
Download Al's games from http://inventwithpython.com/makinggames_src.zip
Unzip them and play a bit. Then, open a file that ends in .py in a text editor
or IDLE, change variables, save it, and test it out by playing the game again.

Intermediate:
Change a game from inventwithpython, http://www.pygame.org/, or
https://pyweek.org/ into something that looks completely different from the
original with different game mechanics.  Since you're making bigger changes,
save your work with a new file name.

A simple example of this is TheGameThatMarioBeat2.py based on code from wormy.py
[The Game That Mario Beat 2](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/PythonScripts/TheGameThatMarioBeat2.py)

Mastery:
Build your own game starting with a blank document using python and pygame using
the internal documentation for python and pygame and the python and pygame
websites.

- [Fat Math Three](https://pyweek.org/e/fat_math_three/) is a well made,
  choose-your-own-adventure with a math game mechanic made for PyWeek.
- [Endgame: Singularity](http://www.emhsoft.com/singularity/) is a simulation
  game in written with python, pygame, and numpy that explores the perspective
  of an AI.  [Source code](https://github.com/singularity/singularity) is on
  github.
- [Video tutorial series from TheNewBoston](https://thenewboston.com/videos.php?cat=120)




## Photo Editing

To add your own images to games, you need to use a photo editor.
[GIMP (the GNU Image Manipulation Program)](https://www.gimp.org/) is free and
open source and works on the Raspberry Pi 3, GNU/Linux, Mac, and Windows.

The default layout has three windows (tools, image, and layers) and can be
confusing to young kids.  On the menu bar, choose Window and "Single-Window
Mode" to make it easier to navigate.

Beginner:
To familiarize yourself with it, take an image from PyGame or Ren'Py and make
some changes to it.  Export it into the same format and test the python script
to make sure it works.

Intermediate:
Use a picture from the Internet.  If you are planning on using the image for a
public project, make sure you have the right to reuse the image.  Bring the
image into GIMP.  In the layers panel, right click on the image layer and choose
"Add Alpha Channel" which adds the ability to have a transparent background.
Crop the character, sprite, or object so that everything else is a checkerboard
pattern.  Save it as a png file.  Try using this png with python in a pygame
activity.  You could also take a photo of yourself with a camera, open the photo
with GIMP, crop your body or face so that the background is transparent, save
the image, and test with python.


## Minecraft: Pi Edition

Minecraft is the best selling game of all time.  Mojang (the original developer
of Minecraft) wrote a version specifically for the Raspberry Pi.  Mojang gave it
alway for free in hopes of teaching youth programming.  Python and java modules
accompany the game.  Minecraft: Pi Edition and the python and java modules are
already installed on Raspbian.

NOTE: Minecraft: Pi Edition only works for the Raspberry Pi's CPU architecture
ARM.  Since the game itself is not open source, it cannot be recompiled for
other computers.  To work with Minecraft: Pi Edition on a 32 or 64 bit CPU
architecture, you have to emulate a Raspberry Pi with something like QEMU (more
on that in the projects section).

Start up Minecraft: Pi Edition.

NOTE: Do not make the game full-screen.  Children tend to do this first thing.
The mouse will not work optimally, and it is not meant to be full-screen.  It is
meant to take up some of the screen while you code next to it.

Create a world and start to play.  Notice the three cartesian coordinates in the
top left corner of the screen.  These coordinates give numbers to the x, y, and
z axis of the game world.

Open up leafpad to code in a text file, or type ''python'' into the terminal to
code in an interactive Python shell, and we will write a program for Minecraft.

```
# import the modules
from mcpi import block
from mcpi import minecraft

# First make a connection between Python and the game
mc = minecraft.Minecraft.create()

# mc is a object we can call to control the world.  Let's say, ''Hello!''
mc.postToChat("Hello, Minecraft World!")

# Now add a block.  You could read the coordinates in the top left, and choose
# numbers near those.
mc.setBlock(-7, 10,0 , block.STONE)

# Try to spell a word in the sky.  It is very easy with copy and paste.
mc.setBlock(-7, 9, 0, block.STONE)
mc.setBlock(-7, 8, 0, block.STONE)
mc.setBlock(-7, 7, 0, block.STONE)
mc.setBlock(-7, 6, 0, block.STONE)
mc.setBlock(-7, 9, 1, block.STONE)
mc.setBlock(-7, 10, 2, block.STONE)
mc.setBlock(-7, 9, 3, block.STONE)
mc.setBlock(-7, 10, 4 , block.STONE)
mc.setBlock(-7, 9, 4, block.STONE)
mc.setBlock(-7, 8, 4, block.STONE)
mc.setBlock(-7, 7, 4, block.STONE)
mc.setBlock(-7, 6, 4, block.STONE)
# I spelled the letter M.  Try to write your name and impress your friends.
```

If you typed this into a file, save it as minecrafthack.py and run it with
''python minecrafthack.py''

Something is not right.  We will have to fix it.  See if you can fix my capital
M.

See if you can write your entire name.

There are other projects that can be found elsewhere like the interactive photo
booth, giant clock, and more.

[minecrafthack.py](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/PythonScripts/minecrafthack.py)

This is only the beginning of what can be done.  Check out these links for more
Minecraft projects with the pi.

- [Raspberry Pi page about Minecraft: Pi Edition](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/)
- [Minecraft Pi api reference](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)
- [An overview about Minecraft Pi programming with links](http://www.stuffaboutcode.com/p/minecraft.html)
- [How to connect Python to regular Minecraft using bukkit server](http://www.stuffaboutcode.com/2013/06/programming-minecraft-with-bukkit.html)
- [How to connect Python to regular Minecraft using canary server](http://www.stuffaboutcode.com/2014/10/minecraft-raspberryjuice-and-canarymod.html)
- [Getting started with Minecraft: Pi](https://github.com/raspberrypilearning/getting-started-with-minecraft-pi)
- [Working clock project for Minecraft Pi](https://github.com/martinohanlon/minecraft-clock)
- [Other projects from that programmer/author Martin](https://github.com/martinohanlon)
- [Minecraft: Pi Edition home page - the api has been updated since then](http://pi.minecraft.net/)
- [Book - Adventures in Minecraft](http://www.amazon.com/Adventures-Minecraft-David-Whale/dp/111894691X/)
- [Book - Learn to Program with Minecraft: Transform Your World with the Power of Python](http://www.amazon.com/Learn-Program-Minecraft-Transform-Python/dp/1593276702/)




## Looping GPIO with Minecraft

Programming Python, loops, GPIO, and Minecraft is all cool, but can we combine
them?  Yes.  Here are two example scripts:

[minecraftlight.py](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/PythonScripts/minecraftlight.py)

[minecraftlightloop.py](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/blob/master/PythonScripts/minecraftlightloop.py)




## Processing

Processing is a great introductory programming language that can make generative
art, interactive art, and drawing.  https://processing.org/

Processing is a programming language about making visual art.  Processing is
geared towards making interactive drawings with code.  It works on Android, iOS,
GNU/Linux, Mac, and Windows.  Drawings can be generated from mouse movements,
music frequencies, GPIO inputs, or web apis.  Processing is one of the easiest
languages to learn.  Processing uses java syntax by default.  You can also use
javascript live on webpages through p5.js.  Python syntax can also be used if
enabled.

To install processing on the Raspberry Pi, run these two commands:

```
wget https://processing.org/download/install-arm.sh

sudo sh install-arm.sh
```

If you want to use P3D, this command will fix a bug in the latest versions of
Raspbian (at the time of this writing):

```
sudo aptitude remove libgles1-mesa libgles2-mesa
```

These are scripts I have made or modified using Processing:

- [JitterTriangles](https://github.com/TechnologyClassroom/Processing/blob/master/JitterTriangles/JitterTriangles.pde)

![Screenshot](https://github.com/TechnologyClassroom/Processing/blob/master/Images/JitterTriangles-29822.png?raw=true "Screenshot")

Generative art using randomly moving triangles of random sizes.  These triangles
have a calming and mesmerizing effect on the viewer.  As this script continues,
the result becomes more unique and beautiful.  Run for an hour to multiple days.
Hold 's' to save images.


- [JitterRotate](https://github.com/TechnologyClassroom/Processing/blob/master/JitterRotate/JitterRotate.pde)

![Screenshot](https://github.com/TechnologyClassroom/Processing/blob/master/Images/JitterRotate-0531.png?raw=true "Screenshot")

JitterRotate is an experiment with semantic errors.  Generative art using
randomly moving triangles of random sizes, colors, rotation, and transparency.
This sketch only takes about 30 seconds to peak.  Hold 's' to save images.


- [PaintWithShapes](https://github.com/TechnologyClassroom/Processing/blob/master/PaintWithShapes/PaintWithShapes.pde)

![Screenshot](https://github.com/TechnologyClassroom/Processing/blob/master/Images/PaintWithShapes.png?raw=true "Screenshot")

Draw with squares, ellipses, and triangles.  Shapes have random fill color,
stroke color, stroke width, and size.  WARNING: Contains flashing lights.  Hold
's' to save images.

The code for my processing examples can be found at my
[Processing github](https://github.com/TechnologyClassroom/Processing).

To learn more, check out the
[Resources section](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#resources)
and my page of
[examples](https://github.com/TechnologyClassroom/Processing/blob/master/ProcessingExamples.md).

Note: Java is licensed under the
[Oracle Binary Code License](http://www.oracle.com/technetwork/java/javase/terms/license/index.html)
which differs from many of the other licenses discussed around the Raspberry Pi.




## Computer Vision: opencv-python and simplecv

I will not demonstrate Computer Vision, but I have to mention it.  ''opencv''
allows you to program the sense of sight.  Analyze photos, video, or live feeds
and make decisions based on what you "see."  It is a very powerful module for
Python.  ''simplecv'' makes it much easier to write programs.  OpenCV is a
framework that works on top of C++, Java or Python.

To learn more, check out the
[Resources section](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#resources).




## Taking The Raspberry Pi Further

Programming on the Raspberry Pi is one of my favorite activities, but I
understand that not everyone is as passionate about code as I am.  There are
many different directions you can take with the Raspberry Pi that have nothing
to do with code.  This section is full of projects, solutions, and resources to
use the Raspberry Pi in creative ways.




## Projects

- Raspberry Pirate Radio

Have you ever wanted to run your own radio station?  You can turn your Raspberry
Pi into an FM radio transmitter using one wire and a Python script.

Notice: If the project was left running in the United States, the FCC could
track you down for using improper signals.  The problem is that depending on the
frequency you use, you could be interfering with frequencies used by emergency
services.  The reason for this is the makeshift antenna and program sends out
block shaped radio waves instead of sine waves.  This spills over to other
frequencies unintended by the program.

http://www.instructables.com/id/Raspberry-Pirate-Radio/

http://makezine.com/projects/raspberry-pirate-radio/

http://lifehacker.com/start-a-pirate-radio-station-with-a-raspberry-pi-and-a-1538837219

http://myhowtosandprojects.blogspot.com/2014/04/raspberry-pi-make-your-own-pirate-radio.html

- Build a robot

If you can power a light with GPIO pins, you can just as easily connect it to a
motor.  Add more motors and you have a robot.

http://diyhacking.com/raspberry-pi-robot/

[Book - Make a Raspberry Pi-Controlled Robot: Building a Rover with Python, Linux, Motors, and Sensors By Wolfram Donat](http://shop.oreilly.com/product/0636920031994.do)

- Create your own web server

What better way to learn web design than creating your own web server?  You can
turn a Raspberry Pi into an entire web stack.  ''LAMP'' stacks are very popular
among the industry (GNU/Linux + Apache + MySQL + PHP).  I prefer using smaller
programs to accomplish nearly the same thing.  I use GNU/Linux + Nginx + SQLite
+ PHP (LNSP) when using a web stack on the Raspberry Pi.  These can also
interact with Python.

https://wiki.archlinux.org/index.php/Nginx


- Create your own Baby Monitor

Most of the "smart" baby monitors on the market are always on devices connected
to the Internet that you do not control.  I built my own with
[PiCam](https://github.com/iizukanao/picam).  It can record to a file or stream
on your local area network (LAN).

```
# If you have not enabled camera, enable it with raspi-config then reboot
sudo raspi-config

# Install dependencies
sudo apt-get update
sudo apt-get install -y libharfbuzz0b
sudo apt-get install -y libfontconfig1

# Create directories and symbolic links
cat > make_dirs.sh <<'EOF'
DEST_DIR=~/picam
SHM_DIR=/run/shm
mkdir -p $SHM_DIR/rec
mkdir -p $SHM_DIR/hooks
mkdir -p $SHM_DIR/state
mkdir -p $DEST_DIR/archive
ln -sfn $DEST_DIR/archive $SHM_DIR/rec/archive
ln -sfn $SHM_DIR/rec $DEST_DIR/rec
ln -sfn $SHM_DIR/hooks $DEST_DIR/hooks
ln -sfn $SHM_DIR/state $DEST_DIR/state
EOF
chmod +x make_dirs.sh
./make_dirs.sh

# Optionally, increase microphone volume with alsamixer
#alsamixer

# Install picam binary
wget https://github.com/iizukanao/picam/releases/download/v1.4.6/picam-1.4.6-binary.tar.xz
tar xvf picam-1.4.6-binary.tar.xz
cp picam-1.4.6-binary/picam ~/picam/

# Run picam
#cd ~/picam
#./picam --alsadev hw:1,0

# Install nginx
sudo apt-get install -y nginx

# Edit nginx configuration
echo "Within the server { ... } block add these lines:"
echo "	location /hls/ {"
echo "		root /run/shm;"
echo "	}"

#	location /hls/ {
#		root /run/shm;
#	}
sudo nano /etc/nginx/sites-available/default

# Set Picam to start automatically
echo "Before exit 0, add this line:
echo "/home/pi/picam-1.4.6-binary/picam -o /run/shm/hls --alsadev hw:1,0"

# /home/pi/picam-1.4.6-binary/picam -o /run/shm/hls --alsadev hw:1,0

sudo nano /etc/rc.local

echo "Find your local IP address."
ip a

sudo reboot
```

On another machine, test your stream.

VLC can open video streams.  Kodi can open streams with the surveillance camera
add-on.

My address was:
http://192.168.1.208/hls/index.m3u8

https://github.com/iizukanao/picam


- Universal Translator

This project allows you to convert speech from one spoken language to another.
Record audio of talking, convert the audio to text, translate the text to
another language, and have it read back to you in another language.

http://www.daveconroy.com/turn-raspberry-pi-translator-speech-recognition-playback-60-languages/

https://github.com/dconroy/PiTranslate


- Connect Raspberry Pis to automate your home

The ''Internet of Things'' (IoT) is a way to connect everything together through
the Internet.  Purchasing IoT devices and appliances can be COSTLY unless you do
it yourself.  A single board computer and a little bit of Python knowledge can
start you on the path to creating your own IoT devices.  Slap a Raspberry Pi
onto a garage door, program it to listen for your phone to connect to the
network, and you have an automated garage door.  There are unlimited
possibilities now with single board computers.

http://www.informationweek.com/software/enterprise-applications/10-raspberry-pi-projects-for-learning-iot/d/d-id/1320757

https://www.raspberrypi.org/blog/tag/internet-of-things/

- Build your own camera

The Raspberry Pi foundation has designed two camera modules that can be easily
connected to the Raspberry Pi.  They are the camera and the infrared modules.

[RPi Camera Module](https://www.raspberrypi.org/products/camera-module/)

[RPi Infrared Camera Module](https://www.raspberrypi.org/products/pi-noir-camera/)

[RPi Camera help](https://www.raspberrypi.org/help/camera-module-setup/)

- Emulating a Raspberry Pi on your Computer with QEMU and Windows

[Emulating a Raspberry Pi on your Computer with QEMU and Windows](http://www.pcsteps.com/1199-raspberry-pi-emulation-for-windows-qemu/)

I confirm that it works and covers all pitfalls.  It feels very slow to use
because it is limited by 256mb of allocated RAM.  The advantage of emulating the
Pi on a computer is that the img file can be modified directly.  A custom img
with updated software and all of your programs can then be copied to your SD
card.

- Build a Retro Game system

The RetroPie project aims to turn a Raspberry Pi into a game system.  It
includes an interface called emulationstation and can emulate many of the game
consoles from 1977 to 1998.

To install RetroPie on top of default Raspbian run these commands:

```
sudo apt-get update
    
git clone git://github.com/petrockblog/RetroPie-Setup
    
cd RetroPie-Setup
    
sudo ./retropie_setup.sh
```

The games will need to be copied into the appropriate folder before the console
will appear in the menu.  Logout to the terminal and run this command:

```
emulationstation
```

A popular alternative to this project is to build a RetroPie into a handheld
case using 3D printed cases and a tiny screen.

[Official RetroPie Website](http://blog.petrockblock.com/retropie/)

[3D printing project for a GameBoy style case](http://www.thingiverse.com/thing:382485)

[Micro Arcade Cabinet](https://www.youtube.com/watch?v=5npkz0xY1fo)

- Build your own ''cloud'' server

The term cloud has been confusing the majority of computer users since its
creation.  It simply means you are putting your private data on someone else's
server.  Since you cannot verify that their interests are in your best interest,
the majority of cloud based services cannot be trusted.  You could build your
own cloud!  I will suggest Freedom Box.  It acts as a cloud and more.

[FreedomBox Foundation](https://freedomboxfoundation.org/)

- Talk with all of your friends at once

You can run a server on your Raspberry Pi called mumble that will allow your
friends to all connect and talk to each other at once.

[Mumble Server forum post](https://www.raspberrypi.org/forums/viewtopic.php?f=36&t=8615)

- Design your own case

If you have access to a 3D printer or some spare legos, you can make your own
cases.  You can use any 3D modeling software to design your own 3D shapes to
protect your Raspberry Pi.  Here are some examples of cases that others have
made:

[8 Interesting DIY RPi Case Ideas](http://www.makeuseof.com/tag/8-interesting-diy-raspberry-pi-case-ideas/)

[Thingiverse 3D models Raspberry Pi Results](http://www.thingiverse.com/search?q=raspberry+pi&sa=)

- Try a program out in space

The AstroPi project put some Raspberry Pi computers on the International Space
Station.  You can build a duplicated device using a 3D printer, a Raspberry Pi,
and a Sense Hat.  There are programming competitions regularly that you can
enter.  Your Python experiment can be carried out in space.  The Raspberry Pis
in space even have their own twitter accounts that you can browse.

https://astro-pi.org/

https://www.raspberrypi.org/blog/astro-pi/

https://twitter.com/astro_pi_ir

https://twitter.com/astro_pi_vis

https://vimeo.com/157627149

- Control your stereo over wifi

How cool would it be to use your phone to control the stereo?  You can do that
with the Raspberry Pi.  Put all of your music on a storage device.  Connect your
music collection to your Pi.  Install and configure mpd (Music Player Daemon) on
your Pi.  Connect your Pi to the stereo.  Connect your phone to your Pi through
an MPD app such as MPoD or MPDroid.

```
# Update software repositories, remove unnecessary software, and install mpd.

sudo apt-get update

sudo apt-get remove -y pulseaudio wolfram-engine wolframscript scratch # Removing pulseaudio fixes the volume control problem.  Removing wolfram and scratch speeds up upgrade time.

sudo apt-get upgrade -y

sudo apt-get install -y mpd mpc

# Change ownership of mpd folders to user mpd and group audio.

sudo chown mpd:audio -R /var/lib/mpd

sudo chown mpd:audio -R /var/log/mpd

# Change the settings for mpd.

sudo nano /etc/mpd.conf

# Add a drive formatted with ext4 containing music files.

# Symlink the music drive to the mpd directory.

sudo ln -s /mnt/music1/Audio /var/lib/mpd/music/

# Change the ownership properties of the mounted drive.

sudo chown mpd:audio -R /mnt/music1

# Restart mpd

sudo service mpd restart

# Update mpd database

mpc update --wait

# Check the progress of the database or look for errors.

tail -n 30 /var/log/mpd/mpd.log

```

http://elinux.org/Rpi_Music_Player_Daemon


- Build a media center

Kodi is a powerful media center that can be installed on your Raspberry Pi.  You
can view your video files from a hard drive or stream files from the web.  I
have had the most success with OSMC which can be installed directly from NOOBS
with an Internet connection.

[OSMC]("https://osmc.tv/")


- Build your own tablet

The Raspberry Pi has released a 7 inch touch screen.  Connect the cables to the
Pi, add power, and you have a tablet.

https://www.raspberrypi.org/products/raspberry-pi-touch-display/

- Virtual Network Computing (VNC)

VNC can be used with nearly all computer systems including GNU/Linux, iOS, Mac,
and Windows.  It is a way to share control of a computer across a network or the
Internet.  Today, it is most commonly used for tech support from remote sites.
VNC software can be installed with these commands:

```
sudo apt-get install tightvncserver xtightvncviewer
```

A VNC server can be started with this command:

```
vncserver :1 -geometry 1920x1080 -depth 24
```

Other computers or phones on your network can connect to your Raspberry Pi with
the proper credentials using your local IP address.  IPv4 addresses are four
sets of numbers separated by periods.  An example of an IP address is
192.168.1.58.  Your local IP address can be found using the command:

```
ifconfig | grep inet
```

https://www.raspberrypi.org/documentation/remote-access/vnc/


- Build a surveillance system

Build your own motion detection cameras and have them email you when someone
walks near your car.  Create a camera that emails you a picture of your desk
every hour.  The possibilities are endless.


- What should I wear today?

Create a system to check the temperature and humidity outside.  Based on that
information, the Raspberry Pi could email you what you should wear to stay warm
throughout the year.


- Create interactive installation art

Many artists have included Raspberry Pis into their work.  One of the most
tranquil of such projects is called ''Lichen Ohms Seriatim'' located in
Cambridge, United Kingdom.  Participants carry around a Raspberry Pi with a
screen, bluetooth adapter, headphones, and a battery in a clear plastic
container.   The sounds change as they approach bluetooth beacons referred to as
''lichens.''  This creates an immersive audio/video experience.

https://www.raspberrypi.org/blog/lichen-beacons/

http://www.ludions.com/projects/lichens/


- Build a supercomputer

You can create a [beowulf system](https://en.wikipedia.org/wiki/Beowulf_cluster)
by connecting a bunch of computers together using network cables, GNU/Linux, and
software to make them act as one.

http://www.zdnet.com/article/build-your-own-supercomputer-out-of-raspberry-pi-boards/

[33 Raspberry Pi Cluster](http://coen.boisestate.edu/ece/raspberry-pi/)

[64 Raspberry Pi Cluster](http://www.southampton.ac.uk/mediacentre/features/raspberry_pi_supercomputer.shtml)

[GCHQ's 66 Raspberry Pi Cluster](http://www.gchq.gov.uk/press_and_media/news_and_features/Pages/GCHQs-Raspberry-Pi-Bramble.aspx)

[Pi Zero OTG Cluster](http://blog.alexellis.io/pizero-otg-swarm/)


- Participate with an open source project

Another great way to get more experience is to find a python script on github,
make a github account, and fork the project.  To fork a project, you can take
someone else's program, make changes, and make it your own; or you can make a
change, and submit the change back to the original project.  Even changing a
simple grammar mistake is a great first move.




## Problems and Solutions That Worked for Me

This section is not a comprehensive troubleshooter for a Raspberry Pi, but it
gives some examples of the problem solving skills that will be beneficial to
your journey into microcomputers.  When I bought my model B, a lot of problems
had not been worked out.  Compromises, workarounds, and hacks had to be
implemented to accomplish some goals.  Many of these problems have been solved
with the new line of Raspberry Pis including the A+, B+, 2 B, Zero, and 3 B.

- Low resolution video

This happens with kids ofen.  The quick solution is to reboot.  Click on the
menu in the top left > Logout > Reboot.

This happens when you first plug in the Raspberry Pi with the power before the
HDMI.  If you change the order of operations to HDMI and then power, the boot
process will automatically identify the video source and give provide optimal
resolution.

- Wireless Drivers

Wireless adapters do not always work.  This is because the hardware manufacturer
has closed source, proprietary drivers.  Some brands work very well and others
require extra work to use them.  After doing too much of the extra work, I
always look up the chipset of compatible wireless cards BEFORE I buy a new one.
Atheros chipsets are nearly always compatible.  The packaging rarely says the
name of the chipset so you always have to
[look it up](https://wikidevi.com/wiki/List_of_Wi-Fi_Device_IDs_in_Linux).

- Peripheral power / Powered USB Hub

The B has two USB ports.  I need to plug in a keyboard, a mouse, and a wifi
adapter.  I could plug in the keyboard and mouse at the same time and use it
perfectly with a wired ethernet connection.  I could unplug the keyboard, plug
in the wifi, search for networks.  To enter in a password, I would have to
unplug the mouse, plug the keyboard in, type the password, and then plug in the
mouse.  Just after I got a valid IP address, the wifi adpater would lose power.
It would start up again, connect, and lose power.  This loop would continue
until I unplugged it.  I ordered a powered USB hub off amazon.  Once that
arrived, I could plug in a keyboard, mouse, wifi adapter, and two storage
devices.  The best part about the powered USB hub is that you can power the
Raspberry Pi with a MicroUSB to USB cable.  The drawback after this is that I
was using much more power then before.  I was very surprised when I tried the B+
with four USB slots.  On the B+, I plugged in keyboard, mouse, and wifi directly
in and it worked perfectly.

- Corrupted SD Cards

The operating system traditionally uses either a SD card or a microSD card.  The
firmware of the first production run ruined many SD cards.  The firmware can be
updated and it eventually got better.  I had been running various GNU/Linux
operating systems off of 16GB flash drives for many years at this point.  After
corrupting the same SD card many times, I gave up on the SD card.  I had to use
it to boot from, but I did not have to run the system off of it.  Default
Raspbian has two partitions in its .img file.  One is a boot and the other is
the root.  I modified the boot configuration to boot from /dev/sdb2 instead of
/dev/sda2.  I then used dd to copy the Raspbian img to a flash drive.  That one
still works.

- Audio pops

One of the projects I made turned my Raspberry Pi model B into an mp3 player for
my hi-fi stereo.  I could control it with my iPhone over the network.
Everything talked perfectly together.  The only problem I had was that there
would be a loud pop between each track.  Not only is this annoying, but it could
damage my speakers.  The problem was well known on the Internet and by the
developers.  The problem was that the power would turn off when not in use and
then turn back on.  The power could not be left on using ALSA the default audio
interface on Raspbian.  I solved this problem by installing PulseAudio.  I
configured pulse to remain always on.  This solved my problem.  The Raspberry Pi
B+ and 2 B fixed this problem.

- No HDMI Video Output

I did a programming workshop using my model B.  I introduced what we were doing
on a TV with the Pi.  Later that day, I took it back out and I could not get any
output from the HDMI.  After troubleshooting a few things, it went back in the
bag.  I later give it to my tech team to try to solve the problem.  They
researched ways to troubleshoot the HDMI, they took off the case, and got it to
work.  This was reproducible.  That official case has since been replaced with
legos.

- No hardware clock

Desktop computers typically have a coin sized battery attached to the
motherboard to keep the clock running on the BIOS.  When the Rapsberry Pi gets
turned off, it loses track of time.  When connected to the Internet, this should
not matter as it will get the correct time from a server.  For offline projects,
you must keep this in mind if your program uses specified times.  As a work
around, I boot up the system, set the time manually, reboot, and then the clock
is correct.  An example of this code is:

```
sudo date -s "14 APR 2053 15:34:00"
```


- Language defaults

When installing from NOOBS and even if the language is correctly set at the
bottom, sometimes the language and keyboard is still incorrect with Raspbian.
There is a GUI tool that can help configure this at the Raspberry Pi menu >
Preferences > Raspberry Pi Configuration > Localisation.  I use Set Locale, Set
Timezone, and Set Keyboard in that menu.

To check localization settings, open a terminal and run this command:

```
locale
```

If settings are not correct, you can run this command (my preferences are
English United States UTF-8):

```
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
```




## Raspberry Pi Giveaway

We will pick an almost random number using Python.  Everyone gets a number 0 -
n.

```
from random import randint

n = 30 # 31 participants because 0 is a number.

print(randint(0,n))
```

The winner gets a Raspberry Pi!

If you did not win, you can buy the one I did this presentation with at cost.



## Encode QR Code

We can encode a QR code offline on the Raspberry Pi using qrencode.

To install qrencode on the pi run this command:

```
sudo apt-get update && sudo apt-get install -y qrencode
```

We will encode a QR code of this website to a PNG and then display the QR code
with these two commands:

```
qrencode -o qrcode.png 'https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop'

feh -F qrcode.png 
```

For more ideas on using qrencode, check out this
[Linux Magazine link](http://www.linux-magazine.com/Online/Features/Generating-QR-Codes-in-Linux).




## Resources
<!-- replace amazon links with DRM-free ebook links. More at https://ssearch.oreilly.com/?q=raspberry+pi and https://ssearch.oreilly.com/?q=linux more at more at https://ssearch.oreilly.com/?q=python -->
This section contains websites and books for everything you ever wanted to know
about the Raspberry Pi, GNU/Linux, Python, Processing, and Computer Vision.

Raspberry Pi Links:

- [RPi Hub on eLinux](http://elinux.org/RPi_Hub)
- [Official Raspberry Pi website](http://www.raspberrypi.org/)
- [Raspberry Pi Subreddit](http://www.reddit.com/r/raspberry_pi/)
- [Raspberry Pi projects from Make Magazine](http://makezine.com/category/technology/raspberry-pi/?post_type=projects)
- [Ask questions on RPi Stack Exchange](http://raspberrypi.stackexchange.com/)
- [RPi channel on Instructables](http://www.instructables.com/tag/type-id/category-technology/channel-raspberry-pi/)
- [RPi tags on Instructables](http://www.instructables.com/tag/type-id/?sort=none&q=raspberry+pi)
- [RPi contest on Instructables](http://www.instructables.com/contest/RaspberryPi/)
- [RasPi.TV blog](http://raspi.tv)
- [Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk)
- [RPi tags on LifeHacker](http://lifehacker.com/tag/raspberry-pi)
- [RPi tags on Hackaday](http://hackaday.com/tag/raspberry-pi/)
- [Raspberry Pi news on Google News](http://news.google.com/news?gl=us&pz=1&ned=us&hl=en&q=raspberry+pi)
- [RPi Beginner channel on Youtube](http://www.youtube.com/user/RaspberryPiBeginners/videos)
- [RPi playlist on Youtube](http://www.youtube.com/playlist?list=PLI2skf6QZ_a3aAhRn1g_lknX-NHgmp14X)
- [RaspberryPiliz channel on Youtube](http://www.youtube.com/user/raspberrypiliz/videos)
- [Raspberry Pi Pod Podcast](http://www.recantha.co.uk/blog/)
- [RasPiFeed](http://raspifeed.com/)
- [Pi Cases Subreddit](https://www.reddit.com/r/picases)
- [Projects from Raspberry Pi.org](https://www.raspberrypi.org/resources/make/)
- [Program beats with Sonic Pi](http://sonic-pi.net/)
- [Programming music with Supercollider and Overtone on the Pi](http://sam.aaron.name/2012/11/02/supercollider-on-pi.html)
- [Node-RED "a visual tool for wiring the Internet of Things"](http://nodered.org/)
- [Free Video Presentation: Using Raspberry Pi and Arduino to survive a zombie apocalypse By Simon Monk](https://www.oreilly.com/ideas/using-your-maker-skills-to-survive-a-zombie-apocalypse)
- [Wolfram cloud based programming language and Mathematica have free versions included on Raspbian.](http://www.wolfram.com/raspberry-pi/)
  For more information, see the
  [wolfram reference](http://reference.wolfram.com/language/).
  
Raspberry Pi Books:

- [MagPi Magazine - Free digital magazines](https://www.raspberrypi.org/magpi/issues/)
- [Raspberry Pi Geek Magazine](http://www.raspberry-pi-geek.com/)
- [Make: Getting Started with Raspberry Pi: Electronic Projects with the Low-Cost Pocket-Sized Computer](http://www.amazon.com/Make-Raspberry-Electronic-Projects-Pocket-Sized/dp/1457186128/)
- [Make: Getting Started with Raspberry Pi](http://www.amazon.com/Getting-Started-Raspberry-Pi-Electronic/dp/1457186128/)
- [Make: a Raspberry Pi-Controlled Robot: Building a Rover with Python, Linux, Motors, and Sensors](http://www.amazon.com/Make-Raspberry-Pi-Controlled-Robot-Building/dp/1457186039)
- [Adventures in Minecraft](http://www.amazon.com/Adventures-Minecraft-David-Whale/dp/111894691X/)
- [Learn to Program with Minecraft: Transform Your World with the Power of Python](http://www.amazon.com/Learn-Program-Minecraft-Transform-Python/dp/1593276702/)
- [FREE Raspberry Pi User Guide](http://www.cs.unca.edu/~bruce/Fall14/360/RPiUsersGuide.pdf)
- [FREE Raspberry Pi: Measure, Record, Explore.](https://leanpub.com/RPiMRE)
- [Programming the Raspberry Pi, Second Edition: Getting Started with Python](http://www.amazon.com/gp/product/1259587401/)
- [Make: Getting Started with Raspberry Pi: Electronic Projects with Python, Scratch, and Linux](http://www.amazon.com/Make-Raspberry-Electronic-Projects-Pocket-Sized/dp/1457186128/)
- [Make: Action: Movement, Light, and Sound with Arduino and Raspberry Pi](http://www.amazon.com/Make-Action-Movement-Arduino-Raspberry/dp/1457187795/)
- [Raspberry Pi Cookbook](http://www.amazon.com/Raspberry-Pi-Cookbook-Simon-Monk/dp/1449365221/)
- [Learning Python with Raspberry Pi](http://www.amazon.com/Learning-Python-Raspberry-Alex-Bradbury/dp/1118717058/)
- [Programming the Raspberry Pi, Second Edition: Getting Started with Python](http://www.amazon.com/Programming-Raspberry-Pi-Second-Edition/dp/1259587401/)
- [Make a Raspberry Pi-Controlled Robot: Building a Rover with Python, Linux, Motors, and Sensors By Wolfram Donat](http://shop.oreilly.com/product/0636920031994.do)
- [Make: Action - Movement, Light, and Sound with Arduino and Raspberry Pi By Simon Monk](http://shop.oreilly.com/product/0636920031901.do)
- [Raspberry Pi For Kids For Dummies By Richard Wentk](http://shop.oreilly.com/product/9781119049517.do)
- [Raspberry Pi Server Essentials By Piotr J. Kula](http://shop.oreilly.com/product/9781783284696.do)
- [Raspberry Pi Projects for Kids, 2nd Edition By Daniel Bates](http://shop.oreilly.com/product/9781785281525.do)
- [Getting Started With Raspberry Pi, 3rd Edition: An Introduction to the Fastest-Selling Computer in the World By Shawn Wallace, Matt Richardson](http://shop.oreilly.com/product/0636920031253.do)
- [Raspberry Pi User Guide By Gareth Halfacree, Eben Upton](http://shop.oreilly.com/product/9781118464465.do)
- [Raspberry Pi Hacks: Tips & Tools for Making Things with the Inexpensive Linux Computer By Ruth Suehle, Tom Callaway](http://shop.oreilly.com/product/0636920029083.do)
- [Free Video Presentation: Intro to Raspberry Pi: be prepared to be inspired to make awesome things By Ed Snajder](http://www.oreilly.com/pub/e/2650)
- [Linux for Makers: Understanding the Operating System That Runs Raspberry Pi and Other Maker SBCs By Aaron Newcomb](http://shop.oreilly.com/product/0636920031338.do)
- [Pay-What-You-Want RPi: Measure, Record, Explore By Malcolm Maclean](https://leanpub.com/RPiMRE)

Programming Links:

- [Learn Programming Subreddit](http://www.reddit.com/r/learnprogramming)
- [Daily Programmer Subreddit](http://www.reddit.com/r/dailyprogrammer)
- [Programming Challenges](http://www.reddit.com/r/programmingchallenges)
- [Free programming books from O'Reilly](http://www.oreilly.com/programming/free/)
- [Free resources from O'Reilly](http://www.oreilly.com/free/)

Python Links:

- [Codecademy's Python track](http://www.codecademy.com/tracks/python)
- [DataCamp's Python Track](https://www.datacamp.com/onboarding/learn?from=home&technology=python)
- [LearnPython.org](http://www.learnpython.org)
- [Python Subreddit](http://www.reddit.com/r/python)
- [pyNES allows you to write original Nintendo games in Python](http://gutomaia.net/pyNES/)
- [Invent With Python](http://inventwithpython.com/index.html)
- [Python 3 Documentation](https://docs.python.org/3/download.html)

Python Books:

- [FREE Make Games with Python MagPi ebook](https://www.raspberrypi.org/magpi/issues/essentials-games-vol1/)
- [FREE Programming Book](http://straightedgelinux.com/blog/python/html/index.html)
- [FREE Programming Book epub and examples](http://straightedgelinux.com/blog/python/)
- [FREE Functional Programming in Python By David Mertz](http://www.oreilly.com/programming/free/functional-programming-python.csp?cmp=em-prog-free-na-lgen_safari_20160929)
- [List of free Python books online](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#python)
- [FREE Snake Wrangling for Kids](http://www.briggs.net.nz/snake-wrangling-for-kids.html)
- [Python for Kids: A Playful Introduction to Programming](http://www.amazon.com/gp/product/1593274076/)
- [Teach Your Kids to Code: A Parent-Friendly Guide to Python Programming](http://www.amazon.com/Teach-Your-Kids-Code-Parent-Friendly/dp/1593276141/)
- [Python Programming for the Absolute Beginner](http://www.amazon.com/gp/product/1435455002/)
- [Hello World! Computer Programming for Kids and Other Beginners](http://www.amazon.com/gp/product/1933988495/)
- [Invent Your Own Computer Games with Python By Al Sweigart](http://shop.oreilly.com/product/9781593277956.do)
- [Python For Kids For Dummies By Brendan Scott](http://shop.oreilly.com/product/9781119093107.do)
- [Instant Pygame for Python Game Development How-to By Ivan Idris](http://shop.oreilly.com/product/9781782162865.do)

Processing Links:

- [Processing Raspberry Pi Wiki](https://github.com/processing/processing/wiki/Raspberry-Pi)
- [Processing home page - includes download links and documentation](https://processing.org/)
- [Online interactive p5.js tutorial through Processing.org.](http://hello.processing.org/)
  If you want more Daniel Sheffman, check out
  [his programming videos on youtube](https://www.youtube.com/user/shiffman/videos)
  and
  [his extensive p5.js vimeo playlist](https://vimeo.com/channels/learningp5js).
- [Processing subreddit](http://www.reddit.com/r/dailyprogrammer) 
- [Online interactive p5.js tutorial through Khan Academy](https://www.khanacademy.org/computing/hour-of-code/hour-of-drawing-code/v/welcome-hour-of-code)
- [Gallery of examples from Hello.Processing](http://hello.processing.org/gallery/)
- [Installing Processing on the Raspberry Pi](http://cagewebdev.com/index.php/raspberry-pi-running-processing-on-your-raspi/)
- [OpenProcessing is an online gallery of Processing sketches and code](http://www.openprocessing.org/)
- [Free MOOC Creative Coding from Future Learn that uses a Processing Curriculum](https://www.futurelearn.com/courses/creative-coding/)
- [Configuring Processing with the Python language.](https://github.com/jdf/processing.py#python-mode-for-processing)

Processing Books and videos for purchase:

- [Make: Getting Started with Processing - A Hands-On Introduction to Making Interactive Graphics By Casey Reas, Ben Fry](http://shop.oreilly.com/product/0636920031406.do)
- [Make: Getting Started with Processing.py - Making Interactive Graphics with Python's Processing Mode By Allison Parrish, Ben Fry, Casey Reas](http://shop.oreilly.com/product/0636920031703.do)
- [Make: Getting Started with p5.js - Making Interactive Graphics in JavaScript and Processing By Lauren McCarthy, Casey Reas, Ben Fry](http://shop.oreilly.com/product/0636920032076.do)
- [The SparkFun Guide to Processing: Create Interactive Art with Code By Derek Runberg](http://shop.oreilly.com/product/9781593276126.do)
- [Learning Processing, 2nd Edition: A Beginner's Guide to Programming Images, Animation, and Interaction By Daniel Shiffman](http://shop.oreilly.com/product/9780123944436.do)
- [Processing 2: Creative Coding Hotshot By Nikolaus Gradwohl](http://shop.oreilly.com/product/9781782166726.do)
- [Processing 2: Creative Programming Cookbook By Jan Vantomme](http://shop.oreilly.com/product/9781849517942.do)
- [Free Nature of Code By Daniel Shiffman](http://natureofcode.com/book/)
- [Video: Processing and Arduino in Tandem: Creating Your Own Digital Art Tools By Joseph Gray](http://shop.oreilly.com/product/0636920013310.do)
- [Video: Processing and Arduino in Tandem: Video Mixer By Joseph Gray](http://shop.oreilly.com/product/0636920018353.do)
- [Video: Processing and Arduino in Tandem: Audio Visualizer By Joseph Gray](http://shop.oreilly.com/product/0636920018377.do)

Computer Vision Links:

- [simplcv](http://simplecv.org/)
- [OpenCV](http://opencv.org/)
- [opencv-python tutorials](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
- [Free PDF book: Programming Computer Vision with Python](http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf)
- [Free Video Presentation: Training Intelligent Camera Systems with Python and OpenCV By Joseph Howse](http://www.oreilly.com/pub/e/3077)

Computer Vision Books:

- [Pay-What-You-Want Instant Raspberry Pi Computer Vision By Ashwin Pajankar](https://leanpub.com/InstantRPiCV)
- [Practical Computer Vision with SimpleCV: The Simple Way to Make Technology See By Kurt Demaagd, Anthony Oliver, Nathan Oostendorp, Katherine Scott](http://shop.oreilly.com/product/0636920024057.do)
- [OpenCV for Secret Agents By Joseph Howse](http://shop.oreilly.com/product/9781783287376.do)
- [Learning OpenCV 3 Computer Vision with Python, 2nd Edition By Joe Minichino, Joseph Howse](http://shop.oreilly.com/product/9781785283840.do)
- [OpenCV Computer Vision with Python By Joseph Howse](http://shop.oreilly.com/product/9781782163923.do)
- [OpenCV with Python By Example By Prateek Joshi](http://shop.oreilly.com/product/9781785283932.do)
- [Learning OpenCV 3: Computer Vision in C++ with the OpenCV Library By Adrian Kaehler, Gary Bradski](http://shop.oreilly.com/product/0636920044765.do)
- [OpenCV 3.0 Computer Vision with Java By Daniel Lelis Baggio](http://shop.oreilly.com/product/9781783283972.do)
- [Learning Image Processing with OpenCV By Gloria Bueno Garcia, Oscar Deniz Suarez, Jose Luis Espinosa Aranda, Jesus Salido Tercero, Ismael Serrano Gracia, Noelia Vallez Enano](http://shop.oreilly.com/product/9781783287659.do)
- [Learning OpenCV: Computer Vision with the OpenCV Library By Gary Bradski, Adrian Kaehler](http://shop.oreilly.com/product/9780596516130.do)
- [Instant OpenCV Starter By Jayneil Dalal, Sohil Patel](http://shop.oreilly.com/product/9781782168812.do)
- [OpenCV 3 Blueprints By Joseph Howse, Steven Puttemans, Quan Hua, Utkarsh Sinha](http://shop.oreilly.com/product/9781784399757.do)
- [OpenCV with Python Blueprints By Michael Beyeler](http://shop.oreilly.com/product/9781785282690.do)
- [OpenCV 2 Computer Vision Application Programming Cookbook By Robert Laganiere](http://shop.oreilly.com/product/9781849513241.do)
- [OpenCV By Example By Prateek Joshi, David Millan Escriva, Vinicius Godoy](http://shop.oreilly.com/product/9781785280948.do)
- [OpenCV Computer Vision Application Programming Cookbook Second Edition By Robert Laganiere](http://shop.oreilly.com/product/9781782161486.do)
- [OpenCV Essentials By Oscar Deniz Suarez, Mª del Milagro Fernandez Carrobles, Noelia Vallez Enano, Gloria Bueno Garcia, Ismael Serrano Gracia, Julio Alberto Paton Incertis, Jesus Salido Tercero](http://shop.oreilly.com/product/9781783984244.do)
- [OpenCV Computer Vision Application Programming By Sebastian Montabone](http://shop.oreilly.com/product/110000051.do)
- [Mastering OpenCV with Practical Computer Vision Projects By Shervin Emami, Khvedchenia Levgen, Naureen Mahmood, Jason Saragih, Roy Shilkrot, David Millan Escriva, Daniel Lelis Baggio](http://shop.oreilly.com/product/9781849517829.do)
- [Android Application Programming with OpenCV 3 By Joseph Howse](http://shop.oreilly.com/product/9781785285387.do)
- [Android Application Programming with OpenCV By Joseph Howse](http://shop.oreilly.com/product/9781849695206.do)
- [OpenCV Android Programming By Example By Amgad Muhammad](http://shop.oreilly.com/product/9781783550593.do)
- [Mastering OpenCV Android Application Programming By Salil Kapur, Nisarg Thakkar](http://shop.oreilly.com/product/9781783988204.do)
- [Instant OpenCV for iOS By Alexander Shishkov, Kirill Kornyakov](http://shop.oreilly.com/product/9781782163848.do)
- [Arduino Computer Vision Programming By Ozen Ozkaya, Giray Yillikci](http://shop.oreilly.com/product/9781783552627.do)



<br>
<br>

This guide was made with a laptop running GNU/Linux, various Raspberry Pi
models, and countless hours of volunteer work and tinkering from open source
programmers.

Python is one of the most fun programming languages.  Remember to have fun with
it and follow your imagination.

[back to top](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop#raspberrypiprogrammingworkshop)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br>
Copyright © Michael McMahon 2015-2018.  Except where otherwise specified, the
text on
[RaspberryPiProgrammingWorkshop](https://github.com/TechnologyClassroom/RaspberryPiProgrammingWorkshop/)
by Michael McMahon is licensed under the
[Creative Commons Attribution-ShareAlike License 4.0 (International) (CC-BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
