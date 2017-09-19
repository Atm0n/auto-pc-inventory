#!/usr/bin/env python3
import network, client
import platform, psutil, cpuinfo
# returns the version and the name of the dist
linux_version = platform.dist()
linux_version = linux_version[0] + " " + linux_version[1]
print(linux_version)
# the date of the last installed update
linux_last_update = platform.version()
print(linux_last_update)
# returns the cpu brand
cpu = cpuinfo.get_cpu_info()
cpu = cpu["brand"]
print(cpu)
# PC NAME
pc_name = platform.node()
print(pc_name)
# returns the processor achitecture
architecture = platform.processor()
print(architecture)
# it stores into a dic all the network data
network = network.network_inf()
print(network)
client.update()
hola = psutil.disk_usage("/")
ram = psutil.virtual_memory()  # all ram info
ram = "RAM: " + str(int(ram[0] / 1000000)) + "MB"
# only what I need :D the total amount
print(ram)
