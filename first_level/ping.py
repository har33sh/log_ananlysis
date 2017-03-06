import socket
import json
import time
import os
from datetime import datetime

class log:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    time=datetime.now().strftime(' [%d-%b-%y %H:%M:%S] ')


def ping_check(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print log.time+  str(ip)+" Reachable"
    except socket.error as e:
        print  log.time+ log.FAIL+ str(ip)+ str(e) + log.ENDC
    s.close()


conf = json.load(open('config.json'))

server_ips=conf["server"]
rpi_ips=conf["rpi"]
camera_ips=conf["camera"]

print log.time+"Checking Servers"
for ip in server_ips:
     ping_check(ip,22)

print log.time+"Checking RPi's"
for ip in rpi_ips:
     ping_check(ip,22)

print log.time+"Checking Cameras"
for ip in camera_ips:
     ping_check(ip,8)
