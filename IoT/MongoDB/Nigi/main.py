import json

from flask import Flask, request, jsonify
from database import get_database
from time import time
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route("/motion-sensors", methods=["GET"])
def get_all_sensors():
    sensors = sensor_collection.find({})
    if sensors:
        return jsonify(json.loads(json_util.dumps(sensors))), 200
    else:
        return jsonify({"error": "No sensors found"}), 404


@app.route("/motion-sensors/<sensor_id>", methods=["GET"])
def get_sensor_by_id(sensor_id):
    sensor = sensor_collection.find_one({"_id": ObjectId(sensor_id)})
    if sensor:
        return jsonify(json.loads(json_util.dumps(sensor))), 200
    else:
        return jsonify({"error": "Sensor not found"}), 404


@app.route("/motion-sensors", methods=["POST"])
def create_sensor():
    data = request.get_json()
    sensor = {
        "manufacturer": data.get("manufacturer"),
        "room": data.get("room")
    }
    sensor_collection.insert_one(sensor)
    return jsonify(json.loads(json_util.dumps(sensor))), 201


@app.route("/motion-sensors/<sensor_id>", methods=["PUT"])
def update_sensor(sensor_id):
    sensor = sensor_collection.find_one({"_id": ObjectId(sensor_id)})
    if sensor:
        data = request.get_json()
        sensor = {
            "manufacturer": data.get("manufacturer"),
            "room": data.get("room")
        }
        sensor_collection.update_one({"_id": ObjectId(sensor_id)}, {"$set": sensor})
        return jsonify(json.loads(json_util.dumps(sensor))), 200
    else:
        return jsonify({"error": "Sensor not found"}), 404


@app.route("/motion-sensors/<sensor_id>", methods=["DELETE"])
def delete_sensor(sensor_id):
    sensor = sensor_collection.find_one({"_id": ObjectId(sensor_id)})
    if sensor:
        sensor_collection.delete_one({"_id": ObjectId(sensor_id)})
        return "", 204
    else:
        return jsonify({"error": "Sensor not found"}), 404


@app.route("/motion-sensors/<sensor_id>/data", methods=["GET"])
def get_sensor_data(sensor_id):
    sensor_data = sensor_data_collection.find({"sensor_id": ObjectId(sensor_id)})
    if sensor_data:
        return jsonify(json.loads(json_util.dumps(sensor_data))), 200
    else:
        return jsonify({"error": "Sensor data not found"}), 404


@app.route("/motion-sensors/<sensor_id>/data", methods=["POST"])
def create_sensor_data(sensor_id):
    sensor_data = {
        "sensor_id": ObjectId(sensor_id),
        "timestamp": time()
    }
    sensor_data_collection.insert_one(sensor_data)
    return jsonify(json.loads(json_util.dumps(sensor_data))), 201


@app.route("/motion-sensors/<sensor_id>/data/<data_id>", methods=["DELETE"])
def delete_sensor_data(sensor_id, data_id):
    sensor_data = sensor_data_collection.find_one({"sensor_id": ObjectId(sensor_id), "_id": ObjectId(data_id)})
    if sensor_data:
        sensor_data_collection.delete_one({"_id": ObjectId(data_id)})
        return "", 204
    else:
        return jsonify({"error": "Sensor data not found"}), 404


# kolko senzorcheta ima 🤙
@app.route("/motion-sensors-cnt", methods=["GET"])
def get_all_sensor_cnt():
    sensors = sensor_collection.count_documents({})
    if sensors:
        return jsonify(json.loads(json_util.dumps(sensors))), 200
    else:
        return jsonify({"error": "No sensors found"}), 404

# kolko zapisa ima v senzoih4eta 🤙
@app.route("/motion-sensors/<sensor_id>/data-cnt", methods=["GET"])
def get_sensor_data_cnt(sensor_id):
    sensor_data = sensor_data_collection.count_documents({"sensor_id": ObjectId(sensor_id)})
    if sensor_data:
        return jsonify(json.loads(json_util.dumps(sensor_data))), 200
    else:
        return jsonify({"error": "Sensor data not found"}), 404

# soihtirhani senzhoihi 🤙
@app.route("/motion-sensors-sorted", methods=["GET"])
def get_all_sensor_sorted():
    sensors = sensor_collection.find({}).sort("manufacturer")
    if sensors:
        return jsonify(json.loads(json_util.dumps(sensors))), 200
    else:
        return jsonify({"error": "No sensors found"}), 404

# limit tuka sus6to taka se srtira
@app.route("/motion-sensors/<sensor_id>/data-limited", methods=["GET"])
def get_sensor_data_lim(sensor_id):
    sensor_data = sensor_data_collection.find({"sensor_id": ObjectId(sensor_id)}).sort("timestamp", -1).limit(2)
    if sensor_data:
        return jsonify(json.loads(json_util.dumps(sensor_data))), 200
    else:
        return jsonify({"error": "Sensor data not found"}), 404

# samo bo6 i tesni
@app.route("/motion-sensors-bo6", methods=["GET"])
def get_all_bo6_sensors():
    sensors = sensor_collection.find({"manufacturer" : {"$ne": "bo6"}})
    if sensors:
        return jsonify(json.loads(json_util.dumps(sensors))), 200
    else:
        return jsonify({"error": "No sensors found"}), 404

## deliit ol
@app.route("/motion-sensors-ol", methods=["DELETE"])
def delete_sensor_ol():
    sensor = sensor_collection.find({})
    if sensor:
        sensor_collection.delete_many({})
        return "", 204
    else:
        return jsonify({"error": "Sensor not found"}), 404


# Ensures that when we start our app using "$ python3 main.py" we'll have a connection to the database
if __name__ == "__main__":

    # used to get the database from the connection defined in database.py
    database = get_database()

    sensor_collection = database["sensors"]
    sensor_data_collection = database["sensor_data"]

    app.run(debug=True, port=5000)
