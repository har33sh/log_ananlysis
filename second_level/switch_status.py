#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from datetime import datetime
from db import write_to_db
from send_mqtt import send_alert
from my_ip import get_ip


GPIO_SSS = 7 #SSS= smart switch status
GPIO.setup(GPIO_SSS,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def smart_switch_status():
    button_state =1-int( GPIO.input(GPIO_SSS))
    if button_state == GPIO.HIGH: #Smart switch is turned ON
        return True
    else: #Smart switch is turned OFF
        return False
