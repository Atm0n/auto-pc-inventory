#!/usr/bin/env python3
import network, client  # imports from the root of the project folder
import platform, psutil, cpuinfo, subprocess  # needed libraies
# returns the version and the name of the dist
data = list()
linux_version = platform.dist()
linux_version = linux_version[1]
data.append(linux_version)


print(linux_version)
# the date of the last installed update
linux_last_update = platform.version()
data.append(linux_last_update)
print(linux_last_update)
# returns the cpu brand
cpu = cpuinfo.get_cpu_info()
cpu = cpu["brand"]
data.append(cpu)
print(cpu)
# PC NAME
pc_name = platform.node()
data.append(pc_name)
print(pc_name)
# pc brand
# LSWH

# returns the processor achitecture
architecture = platform.processor()
data.append(architecture)
print(architecture)
# it stores into a dic all the network data
network = network.network_inf()
data.append(network)
print(network)
# disk = psutil.disk_usage("/")
# print(disk)
ram = psutil.virtual_memory()  # all ram info
ram = int(ram[0] / 1000000)
data.append(ram)
# only what I need :D the total amount
print(ram)
for i in range(0, len(data)):
    print(i)
    print(data)
    client.update(1, i+1, str(data[i]))
