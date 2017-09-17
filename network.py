def network_inf():
    import psutil
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
