#!/bin/bash
FILE=$(date +"%Y-%m-%d-%H-%M")
sshpass -p 'enter your password here' scp -r /home/pi/webcampics/*  Administrator@<enter your instance ip>:c:/webcampics && rm -rf /home/pi/webcampics/*

#sshpass stores the password of ssh session and scp is used to send files to windows VM
#all file locations or path specified can be changed as per wish