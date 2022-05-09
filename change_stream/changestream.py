from pymongo import MongoClient, errors
import time, random
from util import create_connection

inventory = create_connection()

fruits = ['strawberries', 'bananas', 'apples','mango']
for fruit in fruits:
    inventory.insert_one({"type": fruit, "quantity": 100})
print("Staring watch")
try:
    print("Watching!!!!!!")
    with inventory.watch(full_document='updateLookup') as change_stream:
        for data_change in change_stream:
            print(data_change)

except errors.PyMongoError:
    print('Change stream closed because of an error')
