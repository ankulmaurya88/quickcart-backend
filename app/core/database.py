# MongoDB connection
from pymongo import MongoClient
from pymongo.collection import Collection
from app.core.config import MONGO_URI

# client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
# db = client["quickcart"]
client = MongoClient(MONGO_URI)
db = client["quickcart"]
users_collection = db["users"]
