import pymongo
from pymongo import MongoClient
import sys

print("--------EIII")
try:
    client = MongoClient('mongodb://mongo_user:mongo_password@mongodb:27017/')
    db = client["db_test"]

    db_users = db["users"]

    mydict = { "name": "John", "address": "Highway 37" }

    x = db_users.insert_one(mydict)
    
    mydict = { "name": "John", "address": "Highway 38" }
    
    x = db_users.insert_one(mydict)
    
    db.command("serverStatus")
    print("MongoDB connection is up.")
    user_documents = db_users.find({ "name": "John" })
    
    for user in user_documents:
        print(user)
        
except Exception as e:
    print("Error connecting to MongoDB:", e)
    sys.exit(1)