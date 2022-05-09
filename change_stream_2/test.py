from pymongo import MongoClient, errors
from bson.json_util import dumps

clust = "mongodb+srv://Nelson:blessing@cluster0.ieu4h.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(clust)
lessons = client.lessons
test = lessons.test

print(client.changestream.collection.insert_one({'hello':'world'}).inserted_id)