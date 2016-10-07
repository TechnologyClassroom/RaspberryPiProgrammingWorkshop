# setup.sh
# Michael McMahon
# setup.sh recreates my workshop environment from a clean Raspbian

# Run this file on a Raspberry Pi with this command:
# sh setup.sh

# Update repository lists
sudo apt-get update

# Upgrade all packages on the system
sudo apt-get dist-upgrade -y

# Install GPIO module for python
sudo apt-get install -y python-dev
sudo apt-get install -y python-rpi.gpio

# Install Processing
wget https://processing.org/download/install-arm.sh
sudo sh install-arm.sh
# sudo aptitude remove libgles1-mesa libgles2-mesa # Uncomment the beginning of this line to enable P3D.  This disables compatibility with other programs such as mplayer.

# Install additional packages
sudo apt-get install -y fortune
sudo apt-get install -y git
sudo apt-get install -y matchbox-keyboard # On-screen keyboard for optional touch support
sudo apt-get install -y synaptic # GUI for apt-get enables scrolling and searching through available programs
sudo apt-get install -y telnet
# Ascii Art
sudo apt-get install -y aview
sudo apt-get install -y bb
sudo apt-get install -y caca-utils
sudo apt-get install -y cowsay
sudo apt-get install -y figlet
sudo apt-get install -y libaa-bin
sudo apt-get install -y screenfetch
sudo apt-get install -y sl
sudo apt-get install -y xfonts-100dpi
sudo apt-get install -y xfonts-75dpi
sudo apt-get install -y xfonts-base
sudo apt-get install -y xfonts-mona
sudo apt-get install -y xfonts-terminus
sudo apt-get install -y xaos
# Automation
#sudo apt-get install -y ansible
#sudo apt-get install -y italc-client
#sudo apt-get install -y italc-master
#sudo apt-get install -y puppet
#sudo apt-get install -y puppetmaster
sudo apt-get install -y xdotool # Automate keystrokes and mouse actions through bash scripts
# Graphic Design
sudo apt-get install -y feh
sudo apt-get install -y gimp
sudo apt-get install -y imagemagick
sudo apt-get install -y libav-tools # avconv
# Presentation aids
sudo apt-get install -y key-mon # Presentation keyboard and mouse actions
sudo apt-get install -y qrencode # QR Code Encoder
sudo apt-get install -y screenkey # Presentation keyboard actions
# VNC
sudo apt-get install -y tightvncserver
sudo apt-get install -y xtightvncviewer
# Web browsers
sudo apt-get install -y firefox-esr
sudo apt-get install -y lynx # CLI browser
sudo apt-get install -y midori # Lightweight web browser
sudo apt-get install -y youtube-dl
sudo apt-get install -y w3m # CLI browser
# Window Managers
sudo apt-get install -y awesome # Awesome Window Manager

# Backup python_games
cd ~
tar cvf python_games.tar python_games
