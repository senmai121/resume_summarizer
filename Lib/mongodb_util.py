from pymongo import MongoClient

def find_experience(uri):

    client = MongoClient(uri)

# เลือก database และ collection
    db = client["portfolio"]
    collection = db["job_experience"]

# ทดสอบ insert
    #collection.insert_one({"name": "Alice", "age": 30})

# ทดสอบ find
    return collection.find()
       