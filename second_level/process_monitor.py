import commands
import json
import socket
import time
from datetime import datetime
from mqtt_sender import send_msg

def check_status(process_name):
    cmd='ps aux | grep '+process_name +" | wc -l"
    number= int(commands.getstatusoutput(cmd)[1])
    if number > 2:
        return True
    else :
        return False


def get_ip(): #function returns the ip address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("internet.iitb.ac.in",80))
    ip= (s.getsockname()[0])
    s.close()
    return ip


def monitor_process(threadName):
    prev_time=time.time()
    while True:
        for process in process_names:
            if check_status(process)== True:
                cur_time=time.time()
                if(cur_time-prev_time > reset_time):
                    prev_time=time.time()
                    ts=datetime.now().strftime('[%d-%b-%y %H:%M:%S]')
                    msg={"ts":ts,"ip":get_ip(),process:"Running"}
                    msg=json.dumps(msg)
                    send_msg(msg)
            else :
                ts=datetime.now().strftime('[%d-%b-%y %H:%M:%S]')
                msg={"ts":ts,"ip":get_ip(),process:"Not Running"}
                msg=json.dumps(msg)
                send_msg(msg)
        time.sleep(2)


conf = json.load(open('config.json'))
process_names = conf[get_ip()] ["process_names"]
reset_time=conf["reset_time"]
