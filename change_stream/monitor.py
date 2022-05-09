import pymongo
from pymongo import MongoClient, errors
import logging
from util import create_connection

inventory = create_connection()
low_quantity_pipeline = [{'$match': {"fullDocument.quantity": {'$lt': 20}}}]

try:
    print('starting!!!!!!')
    with inventory.watch(pipeline=low_quantity_pipeline, full_document='updateLookup') as change_stream:
        for data_change in change_stream:
            current_quantity = data_change['fullDocument'].get('quantity')
            fruit = data_change['fullDocument'].get('type')
            msg = f'There are only {current_quantity} units of {fruit}'
            print(msg)
except pymongo.errors.PyMongoError:
    logging.error('Change stream closed because of an error')