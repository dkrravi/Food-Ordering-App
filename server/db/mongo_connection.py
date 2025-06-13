import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

try:
    client = MongoClient(MONGO_URI)
    db = client.get_database()  # Uses the database in the URI
    print("✅ MongoDB connected successfully.")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

users_collection = db["users"]
cart_collection = db["cart"]
