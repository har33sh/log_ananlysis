import paho.mqtt.client as mqtt
import json
import time

mqttc = mqtt.Client("Classroom logging")
conf = json.load(open('config.json'))

mqttc.connect(conf["mqttHost"], conf["mqttPort"], conf["mqttKeepalive"])
mqttc.loop_start()

def send_msg(msg):
    mqttc.publish(conf["mqttTopicName"],msg,2)
    print "MQTT msg sent : "+msg
    time.sleep(1)
