#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from datetime import datetime
from mqtt_sender import send_msg
import socket


GPIO_SSS = 7 #SSS= smart switch status
GPIO.setup(GPIO_SSS,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def smart_switch_status():
    button_state =1-int( GPIO.input(GPIO_SSS))
    if button_state == GPIO.HIGH: #Smart switch is turned ON
        return True
    else: #Smart switch is turned OFF
        return False



def get_ip(): #function returns the ip address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("internet.iitb.ac.in",80))
    ip= (s.getsockname()[0])
    s.close()
    return ip


def get_sss(threadName):
    prev_time=time.time()
    while True:
        if smart_switch_status== True:
                cur_time=time.time()
                if(cur_time-prev_time > reset_time):
                    prev_time=time.time()
                    ts=datetime.now().strftime('[%d-%b-%y %H:%M:%S]')
                    msg={"ts":ts,"ip":get_ip(),smart_switch_status:"ON"}
                    msg=json.dumps(msg)
                    send_msg(msg)
        else :
                ts=datetime.now().strftime('[%d-%b-%y %H:%M:%S]')
                msg={"ts":ts,"ip":get_ip(),smart_switch_status:"OFF"}
                msg=json.dumps(msg)
                send_msg(msg)
        time.sleep(2)


conf = json.load(open('config.json'))
reset_time=conf["reset_time"]
