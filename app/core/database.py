# MongoDB connection
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["quickcart"]
users_collection = db["users"]
products_collection = db["products"]
create_cart_collection = db["cart"]

def get_user_collection():
    return users_collection

def get_product_collection():
    return products_collection

def get_cart_collection():
    return create_cart_collection

async def connect_to_mongo():
    global client, db, users_collection, products_collection
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["quickcart"]
    users_collection = db["users"]
    products_collection = db["products"]
    create_cart_collection = db["cart"] # Ensure cart collection is initialized
    print("✅ Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("🛑 MongoDB connection closed")
