# setup.sh
# Michael McMahon
# setup.sh recreates my workshop environment from a clean Raspberry Pi OS.

# Run this file on a Raspberry Pi with this command:
# bash setup.sh

# Update repository lists
sudo apt update

# Upgrade all packages on the system
sudo apt dist-upgrade -y

# Install GPIO module for python
sudo apt install -y python-dev
sudo apt install -y python-rpi.gpio

# Install Processing
wget https://processing.org/download/install-arm.sh
sudo sh install-arm.sh
# sudo aptitude remove libgles1-mesa libgles2-mesa # Uncomment the beginning of this line to enable P3D.  This disables compatibility with other programs such as mplayer.

# Install additional packages
sudo apt install -y fortune
sudo apt install -y git
sudo apt install -y matchbox-keyboard # On-screen keyboard for optional touch support
sudo apt install -y synaptic # GUI for apt-get enables scrolling and searching through descriptions of all available programs
sudo apt install -y telnet
# Ascii Art
sudo apt install -y aview
sudo apt install -y bb
sudo apt install -y caca-utils
sudo apt install -y cowsay
sudo apt install -y figlet
sudo apt install -y libaa-bin
sudo apt install -y screenfetch
sudo apt install -y sl
sudo apt install -y xfonts-100dpi
sudo apt install -y xfonts-75dpi
sudo apt install -y xfonts-base
sudo apt install -y xfonts-mona
sudo apt install -y xfonts-terminus
sudo apt install -y xaos
# Automation
#sudo apt install -y ansible
#sudo apt install -y italc-client
#sudo apt install -y italc-master
sudo apt install -y xdotool # Automate keystrokes and mouse actions through bash scripts
# Graphic Design
sudo apt install -y feh
sudo apt install -y gimp
sudo apt install -y imagemagick
sudo apt install -y libav-tools # avconv
# Presentation aids
sudo apt install -y key-mon # Presentation keyboard and mouse actions
sudo apt install -y qrencode # QR Code Encoder
sudo apt install -y screenkey # Presentation keyboard actions
# VNC
sudo apt install -y tightvncserver
sudo apt install -y xtightvncviewer
# Web browsers
sudo apt install -y firefox-esr
sudo apt install -y lynx # CLI browser
#sudo apt install -y midori # Lightweight web browser
sudo apt install -y youtube-dl
sudo apt install -y w3m # CLI browser
# Window Managers
#sudo apt install -y awesome # Awesome Window Manager
sudo apt install -y i3-wm # i3

# TODO Replace individual commands with a loop. Anyone reading this is encouraged to submit a pull request.

# Backup python_games
cd ~
tar cvf python_games.tar python_games
