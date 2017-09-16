#!/usr/bin/env python3

# network

import psutil
net_inf = dict()
networkinfo = psutil.net_if_addrs()
del networkinfo["lo"]  # this deletes the local host info
nics = networkinfo.keys()
print(nics)  # what gets the network interface names!
for nics in nics:
    print(nics)
    ip = ""
    mac = ""
    net = networkinfo[nics]

    ip = list(net[0])
    print(str(ip[1]) + "help")
    if ip[1] == (mac =:
        # if network isn't connected there's no ip
        ip = " "
        
        mac = net[1]
        mac = mac[2]
        print("hola")
    else:
        ip = ip[1]
        mac = net[2]
        mac = mac[1]

    net_inf[nics] = ip, mac
    print(net_inf)
