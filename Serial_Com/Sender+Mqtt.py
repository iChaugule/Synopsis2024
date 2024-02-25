#!/usr/bin/env python
import time
import serial
# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
  
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("semi/commands")
    # client.subscribe("CoreElectronics/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("\nrecieved from pub:" + msg.topic+" "+ str(msg.payload.decode("utf-8")).rstrip())

    msg_string = str(msg.payload.decode("utf-8")).rstrip()
   
    if str(msg_string).rstrip() == "move front":
        ser.write("front\n".encode('utf-8'))
        print("Received Message:" + msg_string)
        # Do something

    if str(msg_string).rstrip() == "move back":
        ser.write("back\n".encode('utf-8'))
        print("Received Message:" + msg_string)
       # Do something else
       
    if str(msg_string).rstrip() == "stop moving":
        ser.write("stop\n".encode('utf-8'))
        print("Received Message:" + msg_string)
       # Do something else
       
    if str(msg_string).rstrip() == "horn":
        ser.write("horn\n".encode('utf-8'))
        print("Received Message:" + msg_string)
       # Do something else
       
    if str(msg_string).rstrip() == "light on":
        ser.write("light on\n".encode('utf-8'))
        print("Received Message:" + msg_string)
       # Do something else
       
    if str(msg_string).rstrip() == "light off":
        ser.write("light off\n".encode('utf-8'))
        print("Received Message:" + msg_string)
       # Do something else

ser = serial.Serial( port='/dev/ttyACM0', baudrate = 9600, timeout=1)
time.sleep(3)
ser.reset_input_buffer()

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
