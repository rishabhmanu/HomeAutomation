# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
import time

# publish.single("CoreElectronics/test", "Hello", hostname="test.mosquitto.org")
# publish.single("CoreElectronics/topic", "World!", hostname="test.mosquitto.org")
publish.single("demo1/led1", "Red1", hostname="test.mosquitto.org")
time.sleep(4)
print("Done")
