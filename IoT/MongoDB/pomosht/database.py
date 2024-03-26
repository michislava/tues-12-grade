import certifi
from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://georgievaemillia:1856@cluster0.7ndvqdp.mongodb.net/"


DATABASE_NAME = "iot_mongo_db"


def get_database():
    # create connection using MongoCLient
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

    # return the databes
    return client[DATABASE_NAME]