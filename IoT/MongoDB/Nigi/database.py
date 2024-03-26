from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://nikeci:6esitriaemji@cluster0.bkyeisv.mongodb.net/?retryWrites=true&w=majority&appName=IoTExerciseCluster"

DATABASE_NAME = "Cluster0"


def get_database():
    # create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    # return the database
    print("nigga")
    return client[DATABASE_NAME]


