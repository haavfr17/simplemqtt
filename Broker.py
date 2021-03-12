import paho.mqtt.client as mqtt #import the client1
import time
############

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


def get


broker_address="localhost"





print("creating new instance")

client = mqtt.Client("Ax0087") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
client.subscribe("house/ping/pong", 2)


client.publish("house/ping/pong","ping", 2)
time.sleep(4) # wait
client.loop_stop() #stop the loop


