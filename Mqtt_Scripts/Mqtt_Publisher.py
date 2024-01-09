# MQTT Publish Demo
# Publish two messages, to two different topics
import time
import paho.mqtt.publish as publish

publish.single("semi/commands", "reverse", hostname="test.mosquitto.org")
time.sleep(3)
publish.single("semi/commands", "forward", hostname="test.mosquitto.org")
print("Done")