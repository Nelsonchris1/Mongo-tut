from cgi import test
from pymongo import MongoClient
import datetime



clust = "mongodb+srv://Nelson:blessing@cluster0.ieu4h.mongodb.net/test?retryWrites=true&w=majority"
client =MongoClient(clust)

# print("Listing db names")
# print(client.list_database_names())

db = client.test 

# print("Listing db collection_names")
# print(db.list_collection_names())

todo1 = {
    "names":"Nelson",
    "text": "MY Last todo!",
    "status": "open",
    "tags": [
        "Rust", "coding"
    ],
    "date" : str(datetime.datetime.utcnow())
}

todos = db.todo
# result = todos.insert_one(todo1)
# print("data inserted")

# todo2= [
#     {"name": "Patrick", 
#     "text": "My Second todo!", 
#     "status" : "open",
#     "tags": ["python", "coding"],
#     "date": datetime.datetime.utcnow()},
#     {"name": "Mary",
#     "text": "My third todo!",
#     "status": "open",
#     "tags": ["c++", "coding"],
#     "date": datetime.datetime(2022, 1,2, 10, 45)}
#     ]

# result = todos.insert_many(todo2)
# print("Value inserted")

todo3 = {
    "name": "Patrick",
    "text": "My fourth todo!",
    "status": "open",
    "tags": ["java", "coding"],
    "date": datetime.datetime.utcnow()
}

# result = todos.insert_one(todo3)
# print("4th data included")

#results = todos.find({"name":"Patrick"})
d = datetime.datetime(2022, 2, 16)
results = todos.find({"date": {"$lt": d}})
for result in results:
    print(result)