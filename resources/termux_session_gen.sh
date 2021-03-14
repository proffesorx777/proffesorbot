#!/bin/bash
clear
echo "
Wait Creating ur String Session

"
# Termux session string generator for TeleBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/proffesorx777/proffesorbot/master/telesetup.py
pip3 install telethon
python3 telesetup.py
