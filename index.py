#!/usr/bin/env python3
import MAC
import platform
import psutil

# returns the version and the name of the dist
linux_version = platform.dist()
# the date of the last installed update
linux_last_update = "last update: " + platform.version()

# returns the processor achitecture
architecture = platform.processor()

mac_addrs = MAC.get_mac()  # it stores into a list all the mac addrs
disk = psutil.disk_usage("/")
ram = psutil.virtual_memory()  # all ram info
ram = str(int(ram[0] / 1000000)) + "MB"  # only what I need :D the total amount
print(ram)  # to test

