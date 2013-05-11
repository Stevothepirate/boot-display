#!/bin/bash

ip addr list eth0 |grep "inet " |cut -d' ' -f6|cut -d/ -f1 > /home/pi/i2c-disp/IPe.txt

ip addr list wlan0 |grep "inet " |cut -d' ' -f6|cut -d/ -f1 > /home/pi/i2c-disp/IPw.txt

sudo python /home/pi/i2c-disp/IP.py &
