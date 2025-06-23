from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/mydatabase")
client = MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/")
def home():
    # Insert a test document if not exists
    if collection.count_documents({}) == 0:
        collection.insert_one({"message": "Hello from MongoDB!"})
    
    data = collection.find_one()
    return f"MongoDB says: {data['message']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
