# MongoDB connection
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["quickcart"]
users_collection = db["users"]

def get_user_collection():
    return users_collection

async def connect_to_mongo():
    global client, db, users_collection
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["quickcart"]
    users_collection = db["users"]
    print("✅ Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("🛑 MongoDB connection closed")
