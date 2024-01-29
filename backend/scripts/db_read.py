from pymongo import MongoClient
import json

# Load parameters
with open('params.json') as f:
    params = json.load(f) 

#  
db_name = params["db"]["dbName"]
db_col_name = params["db"]["dbCollection"]
mongo_user = params["db"]["mongo"]["user"]
mongo_pswd = params["db"]["mongo"]["pswd"]
mongo_port = params["db"]["mongo"]["port"]
mongo_URI = params["db"]["mongo"]["URI"]

client = MongoClient(f'{mongo_URI}://{mongo_user}:{mongo_pswd}@{mongo_URI}:{mongo_port}/')
db = client[db_name]    
db_col = db[db_col_name]


# Get all collection names in the database
collection_names = db.list_collection_names()
# Drop each collection
for collection_name in collection_names:
    db_coll = db[collection_name]

    user_documents = db_coll.find({ "key": "John" })
    
    for user in user_documents:
        print(user)

# Close the connection
client.close()