# Business logic for cart
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from app.core.database import get_cart_collection

async def get_cart(db: AsyncIOMotorDatabase, user_id: str):
    return await db.cart.find_one({"user_id": ObjectId(user_id)})

async def create_cart(db: AsyncIOMotorDatabase, user_id: str, items: list):
    cart_data = {
        "user_id": ObjectId(user_id),
        "items": items,
        "total_price": 0.0,  # Add real logic later
    }
    result = await get_cart_collection().insert_one(cart_data)
    return await get_cart_collection().find_one({"_id": result.inserted_id})

async def update_cart(db: AsyncIOMotorDatabase, user_id: str, items: list):
    await get_cart_collection().update_one(
        {"user_id": ObjectId(user_id)},
        {"$set": {"items": items}}
    )
    return await get_cart(db, user_id)

async def delete_cart(db: AsyncIOMotorDatabase, user_id: str):
    return await get_cart_collection().delete_one({"user_id": ObjectId(user_id)})
