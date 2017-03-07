import commands
import json
import socket
import time

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


def main():
    prev_time=time.time()
    while True:
        for process in process_names:
            if check_status(process)== True:
                cur_time=time.time()
                if(cur_time-prev_time > reset_time):
                    prev_time=time.time()
                    print process+" Running"
            else :
                print process+" Not Running"
        time.sleep(2)

if __name__=="__main__":
    conf = json.load(open('config.json'))
    process_names = conf[get_ip()] ["process_names"]
    reset_time=conf["reset_time"]
    main()
