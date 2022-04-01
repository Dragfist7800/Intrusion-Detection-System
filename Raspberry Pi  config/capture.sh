#!/bin/bash
DATE=$(date +"%Y-%m-%d-%H-%M")
fswebcam -r 640x480 -p YUYV -S 2 -D 2 -F 2 /home/pi/webcampics/$DATE.jpg