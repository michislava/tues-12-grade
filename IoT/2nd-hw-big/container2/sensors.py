import json
import requests, threading
import random, time
from datetime import datetime

flaskUrl = "http://127.0.0.1:7800/data"

sensorPost = {"aqi_sensor_1": None, "aqi_sensor_2": None, "aqi_sensor_3": None}

def sensorData(id):
    while True:
        value = random.uniform(10, 200)
        timestamp = datetime.now().isoformat()
        data = {
            "value": value,
            "timestamp": timestamp,
            "device_id": id
        }
        sensorPost[id] = data
        time.sleep(1)

threading.Thread(target=sensorData, args=("aqi_sensor_1",)).start()
threading.Thread(target=sensorData, args=("aqi_sensor_2",)).start()
threading.Thread(target=sensorData, args=("aqi_sensor_3",)).start()

requests.post(flaskUrl, json=sensorPost)
