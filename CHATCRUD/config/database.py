from pymongo import MongoClient

client = MongoClient("mongodb+srv://khalil:khalil@khalilcluster.pb4jl83.mongodb.net/?retryWrites=true&w=majority")

db = client.chat_app

collection_name = db["chat_app"]
