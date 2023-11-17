import json
import requests, threading
import random, time
from datetime import datetime

flaskUrl = "http://127.0.0.1:7800/data"
done = True

sensorPost = {}

def sensorData():
    while done:
        value = random.uniform(10, 200)
        timestamp = datetime.now().isoformat()
        data = {
            "value": value,
            "timestamp": timestamp,
            "device_id": id
        }
        sensorPost = data
        time.sleep(1)

threading.Thread(target=sensorData).start()
threading.Thread(target=sensorData).start()
threading.Thread(target=sensorData).start()

requests.post(flaskUrl, json=sensorPost)
