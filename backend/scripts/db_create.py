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

db.command("serverStatus")

print("MongoDB connection is up. DB created")

# Close the connection
client.close()