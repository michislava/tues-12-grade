import json
import requests, threading
import random, time
from datetime import datetime

flaskUrl = "http://container1:7800/data"

sensorPost = {"aqi_sensor_1": None, "aqi_sensor_2": None, "aqi_sensor_3": None}

done_event = threading.Event()
def sensorData(id):
    while not done_event.is_set():
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

try:
    while True:
        # Wait for two seconds
        time.sleep(1)
        requests.post(flaskUrl, json=sensorPost)

except KeyboardInterrupt:
    done_event.set()
    time.sleep(2)  # Adjust the time as needed
    print("Script terminated.")