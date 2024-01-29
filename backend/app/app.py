from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
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

# FASTAPI

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic model for reading data
class DataKey(BaseModel):
    key: str

# Pydantic model for adding data
class DataEntry(BaseModel):
    key: str
    value: str

@app.get("/read/", response_model=List[DataEntry])
def read_data(data_key: DataKey):
    
    col_documents = db_col.find({ "key": data_key.key })
    
    ret_docs = []
    for document in col_documents:
        ret_docs.append(document)
    return ret_docs

@app.get("/readall/", response_model=List[DataEntry])
def read_data():
    
    col_documents = db_col.find({ "key": "John" })
    
    ret_docs = []
    for document in col_documents:
        ret_docs.append(document)
    return ret_docs

@app.post("/add/", response_model=DataEntry)
def add_data(data_entry: DataEntry):
    
    _ = db_col.insert_one( { "key": data_entry.key, "value": data_entry.value })
    return data_entry  # Replace with actual added item or confirmation

