import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

db_test = mongo_client["db_test"]

db_collection = db_test["data"]

mydict = { "name": "John", "address": "Highway 37" }

x = db_collection.insert_one(mydict)

print('app | ')
print(db_test.list_collection_names())
