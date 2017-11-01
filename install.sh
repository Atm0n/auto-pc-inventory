#!/usr/bin/env bash
echo "welcome to the auto-pc-inventory script this will install the needed packages"
echo "Enter the values then press enter or ctrl+c to cancel"
sleep 2
echo "lets begin"
sleep 1
read mysqlip
read user
read secret
read dbname
sudo mkdir -p "/usr/local/scripts/auto-pc-inventory"
cd "/usr/local/scripts/auto-pc-inventory"
sudo touch auto-pc-inventory.conf
echo $mysqlip > auto-pc-inventory.conf
echo $user >> auto-pc-inventory.conf
echo $mysqlsecret >> auto-pc-inventory.conf
echo $dbname >> auto-pc-inventory.conf
sudo wget https://raw.githubusercontent.com/Atm0n/auto-pc-inventory/master/index.py
apt update && sudo apt install python3 python3-pip -y
pip3 install --upgrade pip
pip3 install psutil py-cpuinfo datetime pymysql
