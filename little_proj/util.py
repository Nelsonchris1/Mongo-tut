import pymongo
from pymongo import MongoClient, errors


#Create and lock onto inventory
def create_connection():
    try:
        clust = "mongodb+srv://Nelson:blessing@cluster0.ieu4h.mongodb.net/test?retryWrites=true&w=majority"
        client = MongoClient(clust)
        lessons = client.lessons
        inventory = lessons.inventory
        print("Connected successfully")
        return inventory

    except errors.PyMongoError:
        print("Conection unsuccessful")