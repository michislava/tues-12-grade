from flask import Flask, render_template, jsonify, request
from pysondb import db
from matplotlib import pyplot as plt
from io import BytesIO

sensorDb = db.getDb("static/data.json")

app = Flask(__name__)

@app.route('/')
def links():
    return render_template("home.html")

@app.route('/data', methods=['POST', 'GET'])
def addData():
    data = request.get_json()
    sensorItem={
        "value": data.get("value"),
        "timestamp": data.get("timestamp"),
        "device_id": data.get("device_id")
    }
    sensorDb.add(sensorItem)
    return "", 200

@app.route('/graph/<sensor_id>', methods=['GET'])
def getData(sensor_id):
    q =  {"device_id": sensor_id}
    sensor_data = sensorDb.getByQuery(query=q)
    print(sensor_data)
    if sensor_data == None:
        return "There is no data."

    sorted_data = sorted(sensor_data, key=lambda x: x.get('timestamp', ''))
    print(sorted_data)

    plt.stem([data['timestamp'] for data in sorted_data], [data['value'] for data in sorted_data])
    plt.xlabel('Timestamp')
    plt.ylabel('Air Quality')
    plt.title('Data')

    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    plt.clf()

    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7800)
