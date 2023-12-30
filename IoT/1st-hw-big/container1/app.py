from flask import Flask, render_template, jsonify, request, send_file
from pysondb import db
from matplotlib import pyplot as plt
from io import BytesIO
import json

sensorDb = db.getDb("static/data.json")

app = Flask(__name__)

def get_sensor_data(sensor_id):
    with open('static/data.json', 'r') as json_file:
        data = json.load(json_file).get('data', [])
    filtered_data = [entry[sensor_id] for entry in data if sensor_id in entry]

    return filtered_data


@app.route('/')
def links():
    sensor_ids = ["aqi_sensor_1", "aqi_sensor_2", "aqi_sensor_3"]
    sensor_links = [f"/graph/{sensor_id}" for sensor_id in sensor_ids]
    return render_template("home.html", sensor_links=sensor_links)

@app.route('/data', methods=['POST', 'GET'])
def addData():
    data = request.get_json()
    sensorItem={
        "aqi_sensor_1": data.get("aqi_sensor_1"),
        "aqi_sensor_2": data.get("aqi_sensor_2"),
        "aqi_sensor_3": data.get("aqi_sensor_3")
    }
    sensorDb.add(sensorItem)
    return "", 200

@app.route('/graph/<sensor_id>', methods=['GET'])
def getData(sensor_id):
    sensor_data = get_sensor_data(sensor_id)

    timestamps = [entry['timestamp'] for entry in sensor_data]
    values = [entry['value'] for entry in sensor_data]
    colors = []

   #Bate uspeshno minava
    for value in values:
        if 0 <= value <= 50:
            colors.append("green")
        elif 51 <= value <= 100:
            colors.append("yellow")
        elif 101 <= value <= 150:
            colors.append("orange")
        elif 151 <= value <= 200:
            colors.append("red")

    fig, ax = plt.subplots()
    plt.figure(figsize=(12, 7))
    for timestamp, value, color in zip(timestamps, values, colors):
        plt.plot([timestamp], [value], marker='o', linestyle='-',  color=color, markeredgecolor='black')

    plt.xlabel('Timestamp')
    plt.ylabel('Air Quality')
    plt.title('Data')

    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    plt.clf()

    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    plt.switch_backend('agg') #Matplotlib da ne troli a da e v "agg" non-interactive backend
    app.run(host='0.0.0.0', port=7800)
