#!/bin/bash
clear
echo "
██████╗░██████╗░░█████╗░███████╗███████╗░██████╗░██████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗
██████╔╝██████╔╝██║░░██║█████╗░░█████╗░░╚█████╗░╚█████╗░██║░░██║██████╔╝
██╔═══╝░██╔══██╗██║░░██║██╔══╝░░██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██║░░░░░███████╗██████╔╝██████╔╝╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝ 

"

echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Anmol-dot283/Black-Lightning/master/resources/lightning-setup.py
pip3 install telethon
python3 telebot-setup.py