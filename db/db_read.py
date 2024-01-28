from pymongo import MongoClient

client = MongoClient('mongodb://mongo_user:mongo_password@mongodb:27017/')

# Select the database
db = client["db_test"]

# Get all collection names in the database
collection_names = db.list_collection_names()
# Drop each collection
for collection_name in collection_names:
    print(f'Name {collection_name}')
    db_coll = db[collection_name]

    user_documents = db_coll.find({ "name": "John" })
    
    for user in user_documents:
        print(user)

# Close the connection
client.close()