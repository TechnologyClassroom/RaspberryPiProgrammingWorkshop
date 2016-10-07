# Run this file on a Raspberry Pi with this command:
# sh LED7withbash.sh
# You will be asked for your password.

# Setup GPIO7 as an output
sudo echo "7" > /sys/class/gpio/export
sudo echo "out" > /sys/class/gpio/gpio7/direction

# Turn GPIO7 on
sudo echo "1" > /sys/class/gpio/gpio7/value

# Wait 1 second
sleep 1

# Turn GPIO7 off
sudo echo "0" > /sys/class/gpio/gpio7/value

# Wait 1 second
sleep 1

# Turn GPIO7 on
sudo echo "1" > /sys/class/gpio/gpio7/value

# Wait 1 second
sleep 1

# Turn GPIO7 off
sudo echo "0" > /sys/class/gpio/gpio7/value

# Wait 1 second
sleep 1

# Turn GPIO7 on
sudo echo "1" > /sys/class/gpio/gpio7/value

# Wait 1 second
sleep 1

# Turn GPIO7 off
sudo echo "0" > /sys/class/gpio/gpio7/value
