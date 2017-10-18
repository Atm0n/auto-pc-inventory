#!/usr/bin/env python3
import network, client  # imports from the root of the project folder
import platform, psutil, cpuinfo, datetime  # needed libraies
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
network = network.network_inf()
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
client.update(data)
