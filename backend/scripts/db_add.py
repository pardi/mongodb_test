from pymongo import MongoClient
import sys
import random
import json


try:
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
    db_col = client[db_name][db_col_name]
    
    new_entry = { "key": "John", "value": f"Highway {random.random()}" }
    
    x = db_col.insert_one(new_entry)
        
except Exception as e:
    print("Error connecting to MongoDB:", e)
    sys.exit(1)
    
    