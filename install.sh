#!/usr/bin/env bash
echo "Welcome to the auto-pc-inventory script!This will install the needed packages"
sudo su
mkdir /usr/local/scripts
mkdir /usr/local/scripts/auto-pc-inventory
chmod 755 /usr/local/scripts/auto-pc-inventory
touch /usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf
echo "Enter the values then press ENTER or CTRL+C to cancel"

echo "lets begin"
echo "ip"
read ip

echo "user"
read -r "halp" user
echo "secret"
read secret
echo "dbname"
read dbname
echo "$mysqlip
$user
$mysqlsecret
$dbname"< sudo /usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf

wget https://raw.githubusercontent.com/Atm0n/auto-pc-inventory/master/index.py -P /usr/local/scripts/auto-pc-inventory/
apt update && sudo apt install python3 python3-pip -y
pip3 install --upgrade pip
pip3 install psutil py-cpuinfo datetime pymysql
