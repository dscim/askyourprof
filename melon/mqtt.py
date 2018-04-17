import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("ttm4115/team18/", qos=2)

def on_message(client, userdata, msg):
    print(msg.payload.decode())

def setProf(self, prof):
    self.prof = prof

def getProf(self):
    return self.prof

prof = None

client = mqtt.Client("webserver_team18", clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883)
