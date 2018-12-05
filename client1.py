# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("CoreElectronics/test")
    # client.subscribe("CoreElectronics/topic")
    client.subscribe("demo1/led1")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    s = msg.payload
    print(msg.topic+" "+str(msg.payload))
    # print("haha")
    print(msg.payload.decode("utf-8"))
    if "Red1on" in msg.payload.decode("utf-8"):
        print("Red1 On!")
        GPIO.output(5, 1)
        # Do something
    elif "Red2on" in msg.payload.decode("utf-8"):
        print("Red2 On!")
        GPIO.output(13, 1)
        # Do something else
    elif "Whiteon" in msg.payload.decode("utf-8"):
        print("White On!")
        GPIO.output(11, 1)
        #Do Something else
    elif "Red1off" in msg.payload.decode("utf-8"):
        print("Red1 off!")
        GPIO.output(5, 0)
    elif "Red2off" in msg.payload.decode("utf-8"):
        print("Red2 Off!")
        GPIO.output(13, 0)
    elif "Whiteoff" in msg.payload.decode("utf-8"):
        print("White off!")
        GPIO.output(11, 0)
    # print("haha again")

#setting up the connections
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
