#!/usr/bin/env python3

# network

def get_mac():
    import psutil
    macs = list()
    network_info = psutil.net_if_addrs()
    del network_info["lo"]  # this deletes the local host info
    nics = network_info.keys()  # what gets the network interface names!
    for i in nics:
        mac1 = network_info[i]
        mac1 = mac1[2]
        mac1 = mac1[1]
        macs.append(mac1)
