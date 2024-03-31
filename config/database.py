from pymongo import MongoClient

#put your own URI for mongodb <username>:<password> have to be changed
client = MongoClient()

db = client.todo_db

collection_name = db["todo_collection"]
