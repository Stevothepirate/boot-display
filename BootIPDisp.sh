#!/bin/bash

ip addr list eth0 |grep "inet " |cut -d' ' -f6|cut -d/ -f1 > IPe.txt

ip addr list wlan0 |grep "inet " |cut -d' ' -f6|cut -d/ -f1 > IPw.txt

sudo python IP.py &
