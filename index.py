#!/usr/bin/env python3
import network, client  # imports from the root of the project folder
import platform, psutil, cpuinfo, datetime  # needed libraies
# returns the version and the name of the dist
data = list()
date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
data.append(date)
linux_version = platform.dist()
linux_version = linux_version[1]
data.append(linux_version)
# the date of the last installed update
linux_last_update = platform.version()
data.append(linux_last_update)
# returns the cpu brand
cpu = cpuinfo.get_cpu_info()
cpu = cpu["brand"]
data.append(cpu)
# PC NAME
pc_name = platform.node()
data.append(pc_name)
# pc brand
# LSWH
# returns the processor achitecture
architecture = platform.processor()
data.append(architecture)
# it stores into a dic all the network data
network = network.network_inf()
net_keys = list(network.keys())
mac = list()
for i in range(0, len(net_keys)):
    key = net_keys[i]
    if key[0:3] == "wlp":
        network_wlan = network[key]
        network_wlan = network_wlan["mac"]
        mac.append(network_wlan)
    elif key[0:3] == "enp":
        network_eth = network[key]
        network_eth = network_eth["mac"]
    else:
        pass
# suposing that there are only 2 network interfaces, if not, you have to fix it XD
data.append(network_wlan)  # wireless
data.append(network_eth)    # ethernet

ram = psutil.virtual_memory()  # all ram info
ram = int(ram[0] / 1000000)
data.append(ram)

for i in range(0, len(data)):
    client.update(2, i+1, str(data[i]))
