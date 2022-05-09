from pymongo import MongoClient, errors
import random, time


clust = "mongodb+srv://Nelson:blessing@cluster0.ieu4h.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(clust)

lessons = client.lessons
inventory = lessons.inventory

fruits = ["strawberries", 'banana', 'apples', 'mango']
quantities = [-1, -2, -4, -8]

while True:
    print('started!!!')
    random_fruit = random.choice(fruits)
    random_quantity = random.choice(quantities)
    inventory.update_one({'type': random_fruit, 'quantity': {"$gt": 10} }, {"$inc":{"quantity": random_quantity}} )
    time.sleep(1)