import paho.mqtt.client as mqtt #import the client1
import time


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
    if str(message.payload.decode("utf-8")) == "ping" :
        client.publish(str(message.topic),"pong")
        print("ponged")

print("Input qos wanted")
qos = int(input())
print("using qos")

broker_address="localhost"

print("creating new instance")

client = mqtt.Client("Ponger") #create new instance
client.on_message=on_message #attach function to callback


print("connecting to broker")
client.connect(broker_address) #connect to broker


client.loop_start() #start the loop
client.subscribe("house/ping/pong", qos)
print("subed to house/ping/pong")

while True:
    time.sleep(2)




client.loop_stop() #stop the loop
