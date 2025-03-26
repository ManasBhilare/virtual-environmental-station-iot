import requests
import json
import time
import paho.mqtt.client as mqtt

API_KEY = "FYLXS19FOXT98U5J"
URL = "https://api.thingspeak.com/update"
TOPIC = "environment/station1"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("Received:", payload)

        response = requests.post(URL, params={
            "api_key": API_KEY,
            "field1": payload.get("temperature"),
            "field2": payload.get("humidity"),
            "field3": payload.get("co2")
        })

        print("Data sent to ThingSpeak:", response.status_code)
    except Exception as e:
        print("Error:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
