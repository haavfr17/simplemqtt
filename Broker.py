import paho.mqtt.client as mqtt #import the client1
import time
############

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)




broker_address="localhost"

print("Input qos wanted")
qos = int(input())
print("using qos")




print("creating new instance")

client = mqtt.Client("Ax0087") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
client.subscribe("house/ping/pong", qos)


while True:
    print("Input what you want to publish or input exit to close \n")
    user_message = str(input())
    print("wait 1 second before entering new message")
    time.sleep(1)
    if user_message == "exit":
        print("Closing down")
        break
    client.publish("house/ping/pong", user_message)


client.loop_stop() #stop the loop


