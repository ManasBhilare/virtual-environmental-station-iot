import random
import time
import paho.mqtt.client as mqtt
import json

BROKER = "mqtt.eclipseprojects.io"
TOPIC = "environment/station1"
CLIENT_ID = "virtual_station_001"

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.connect(BROKER, 1883, 60)
client.loop_start()

try:
    while True:
        data = generate_sensor_data()
        client.publish(TOPIC, json.dumps(data))
        print(f"Published: {data}")
        time.sleep(10)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
