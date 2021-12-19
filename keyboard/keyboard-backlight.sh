#!/bin/sh
value=`cat /sys/class/leds/input10::scrolllock/brightness`
if [ $value  = "1" ]
then
sudo sh -c 'echo "0" > /sys/class/leds/input10::scrolllock/brightness'
else
sudo sh -c 'echo "1" > /sys/class/leds/input10::scrolllock/brightness'
fi
