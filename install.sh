#!/usr/bin/env bash
echo "welcome to the auto-pc-inventory script this will install the needed packages"
echo "You need root permissions.Enter the values then press enter or ctrl+c to cancel"
echo "lets begin"
echo "enter the mysql server ip"
read mysqlip
echo "enter the mysql user name"
read user
echo "enter the mysql secretpass"
read secret
echo "enter the dbname"
read dbname
echo "Now enter the administrator password"
sed -i '/exit 0/d' /etc/rc.local
echo "/usr/local/scripts/auto-pc-inventory/start.sh" >> /etc/rc.local
echo "exit 0" >> /etc/rc.local
mkdir -p "/usr/local/scripts/auto-pc-inventory"
chmod 755 "/usr/local/scripts/auto-pc-inventory"
touch "/usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf"
echo $mysqlip,$user,$secret,$dbname  > "/usr/local/scripts/auto-pc-inventory/auto-pc-inventory.conf"
cd "/usr/local/scripts/auto-pc-inventory"
touch start.sh
echo "#!/bin/sh
sleep 60
while ! ping -c1 $mysqlip >/dev/null
    do echo error > /dev/null
done
python3 "/usr/local/scripts/auto-pc-inventory/index.py"" > start.sh
chmod 2744 start.sh
sudo wget https://raw.githubusercontent.com/Atm0n/auto-pc-inventory/master/index.py
sudo apt update && sudo apt install python3 python3-pip -y
pip3 install --upgrade pip
pip3 install psutil py-cpuinfo datetime pymysql
