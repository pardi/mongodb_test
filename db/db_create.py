from pymongo import MongoClient

client = MongoClient('mongodb://mongo_user:mongo_password@mongodb:27017/')

# Select the database
db = client["db_test"]

db_users = db["users"]

db.command("serverStatus")

print("MongoDB connection is up. DB created")

# Close the connection
client.close()