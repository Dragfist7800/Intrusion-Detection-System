#!/bin/bash
FILE=$(date +"%Y-%m-%d-%H-%M")
sshpass -p 'your password' scp -r /home/pi/webcampics/*  Administrator@<'your instance ip here'>:c:/webcampics && rm -rf /home/pi/webcampics/*