import time
#import paho.mqtt.publish as publish

while True:

  cmd = input("Please enter the command: ")
  
  cmd = cmd.lower()
  print(f"Recognized {cmd}")

  #publish.single("semi/commands", cmd, hostname="test.mosquitto.org")
