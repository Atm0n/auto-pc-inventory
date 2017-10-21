#!/usr/bin/env bash
echo "welcome to the auto-pc-inventory script this will install the needed packages"
sudo su
mkdir /usr/local/scripts
mkdir /usr/local/scripts/auto-pc-inventory
chmod 755 /usr/local/scripts/auto-pc-inventory
touch /usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf
echo "Enter the values then press enter or ctrl+c to cancel"
echo "lets begin"
read -p mysqlip
read -p user
read -p secret
read -p dbname
echo "$mysqlip" </usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf
echo "$user" <</usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf
echo "$mysqlsecret" <</usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf
echo "$dbname" <</usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf

wget https://raw.githubusercontent.com/Atm0n/auto-pc-inventory/master/index.py -P /usr/local/scripts/auto-pc-inventory/
apt update && sudo apt install python3 python3-pip -y
pip3 install --upgrade pip
pip3 install psutil py-cpuinfo datetime pymysql
