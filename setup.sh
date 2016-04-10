# Run this file on a Raspberry Pi with this command:
# sh setup.sh
# You will be asked for your password.

sudo apt-get update

# Install Synaptic for viewing available programs
sudo apt-get install -y synaptic

# Install GPIO module for python
sudo apt-get install -y python-dev python-rpi.gpio

# Install Processing
wget https://processing.org/download/install-arm.sh
sudo sh install-arm.sh
sudo aptitude remove libgles1-mesa libgles2-mesa

# Install on-screen keyboard for optional touch support
sudo apt-get install -y matchbox-keyboard

# Upgrade all packages on the system
sudo apt-get dist-upgrade -y

# Add additional packages
sudo apt-get install -y git xaos cowsay fortune bb libaa-bin caca-utils aview figlet sl telnet awesome