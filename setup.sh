# setup.sh
# Michael McMahon

# Run this file on a Raspberry Pi with this command:
# sh setup.sh
# You will be asked for your password.

# Update repository lists
sudo apt-get update

# Install Synaptic for viewing available programs
sudo apt-get install -y synaptic

# Install GPIO module for python
sudo apt-get install -y python-dev
sudo apt-get install -y python-rpi.gpio

# Install Processing
wget https://processing.org/download/install-arm.sh
sudo sh install-arm.sh
# sudo aptitude remove libgles1-mesa libgles2-mesa # Uncomment the beginning of this line to enable P3D.

# Install on-screen keyboard for optional touch support
sudo apt-get install -y matchbox-keyboard

# Upgrade all packages on the system
sudo apt-get dist-upgrade -y

# Add additional packages
sudo apt-get install -y feh
sudo apt-get install -y gimp
sudo apt-get install -y git
sudo apt-get install -y telnet
sudo apt-get install -y tightvncserver
sudo apt-get install -y xtightvncviewer
sudo apt-get install -y midori # Lightweight web browser
sudo apt-get install -y firefox-esr
# Ascii Art related packages:
sudo apt-get install -y xaos
sudo apt-get install -y cowsay
sudo apt-get install -y fortune
sudo apt-get install -y bb
sudo apt-get install -y libaa-bin
sudo apt-get install -y caca-utils
sudo apt-get install -y aview
sudo apt-get install -y figlet
sudo apt-get install -y sl
sudo apt-get install -y xfonts-mona
sudo apt-get install -y xfonts-terminus
sudo apt-get install -y xfonts-100dpi
sudo apt-get install -y xfonts-75dpi
sudo apt-get install -y xfonts-base
sudo apt-get install -y screenfetch

