import paho.mqtt.client as mqtt
import paho.mqtt
import time
import json
import pymongo
from pymongo import MongoClient
import sys

def server():

    def on_connect(client, userdata, flags, rc):
        client.subscribe("data/kresit/logs/classrooms/")

    def on_message(client, userdata, msg):
        print msg.payload
        file_name = "test.log"
        write_message = json.loads(msg.payload)
        f = open(file_name, 'a')
        f.write(write_message+"\n")
        f.close()
        print "Written:" + str(write_message) + " Data:" + msg.payload

    client = mqtt.Client(protocol=mqtt.MQTTv31)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("10.129.23.41", 1883, 60)
    client.loop_forever()

server()
