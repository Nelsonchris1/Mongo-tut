from pymongo import MongoClient, errors
import time, random

#Create and lock onto inventory
def create_connection():
    clust = "mongodb+srv://Nelson:blessing@cluster0.ieu4h.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(clust)
    lessons = client.lessons
    inventory = lessons.inventory
    return inventory
