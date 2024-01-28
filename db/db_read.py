from pymongo import MongoClient

client = MongoClient('mongodb://mongo_user:mongo_password@mongodb:27017/')

# Select the database
db = client["db_test"]

# Get all collection names in the database
collection_names = db.list_collection_names()
print(collection_names)
# Drop each collection
for collection_name in collection_names:
    print(collection_name)

# Close the connection
client.close()