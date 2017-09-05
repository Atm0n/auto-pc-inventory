# intent d'algo, 24-8-2017 extrere dades sobre el sistema i posteriorment enviar-les a un servidor que farà d'inventari ?? by: atm0n

import platform, psutil, subprocess, os, re
# SUBPROCESS CACA NO FER SERVIRsi
#windows#########################################3


#linux###############################################
# returns the version and the name of the dist
linux_version = platform.dist()
print("version: " + linux_version[0] + " " + linux_version[1])
# the date of the last installed update
linux_last_update ="last update: " + platform.version()
print(linux_last_update)
# returns the processor achitecture
processor = "cpu architecture: " + platform.processor()
print(processor)
cpu_info = subprocess.check_output("cat /proc/cpuinfo |grep 'model name' ", shell=True).strip()


print ("prova")
print(cpu_info)


############################### psutil
