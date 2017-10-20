#!/usr/bin/env python3
# imports from the root of the project folder
import platform, psutil, cpuinfo, datetime, pymysql  # needed libraies

def update(data):
    

    conn = pymysql.connect(host='192.168.56.101', user='clients', passwd='inventory', db='inventory')
    cur = conn.cursor()
    sql = "DELETE FROM `inventory` WHERE `mac_wlan` = %s"
    cur.execute(sql, (data[6]))
    conn.commit()
    sql = "DELETE FROM `inventory` WHERE `mac_eth` = %s"
    cur.execute(sql, (data[7]))
    conn.commit()
    sql = "INSERT INTO inventory(last_seen,version,cpu,pc_name,arch,RAM, mac_wlan, mac_eth) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    conn.commit()
    conn.close()
def network_inf():
    data_total = {}  # where all the data is stored
    for iface_name, iface in psutil.net_if_addrs().items():
        data = {}  # to avoid residual data
        if iface_name == "lo":
            pass  # if the interface is "lo" (localhost) it's ignored
        else:
            for addr in iface:
                if addr.family == 2:  # IPv4
                    data['ipv4'] = addr.address
                    data_total[iface_name] = data  # to store the ipv4
                elif addr.family == 17:  # MAC
                    data['mac'] = addr.address
                    data_total[iface_name] = data  # to store the mac
    return data_total
# returns the version and the name of the dist
data = list()
date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
linux_version = platform.dist()
linux_version = linux_version[0]+" "+linux_version[1]
# returns the cpu brand
cpu = cpuinfo.get_cpu_info()
cpu = cpu["brand"]
# PC NAME
pc_name = platform.node()
# returns the processor achitecture
architecture = platform.processor()
# it stores into a dic all the network data
network = network_inf()
net_keys = list(network.keys())

for i in range(0, len(net_keys)):
    key = net_keys[i]
    if key[0:2] == "wl":
        network_wlan = network[key]
        network_wlan = network_wlan["mac"]
    elif key[0:1] == "e":
        network_eth = network[key]
        network_eth = network_eth["mac"]
    else:
        pass
# suposing that there are only 2 network interfaces, if not, you have to fix it XD
ram = psutil.virtual_memory()  # all ram info
ram = int(ram[0] / 1000000)

data.append(date)
data.append(linux_version)
data.append(cpu)
data.append(pc_name)
data.append(architecture)
data.append(ram)
data.append(network_wlan)  # wireless
data.append(network_eth)   # ethernet
update(data)
