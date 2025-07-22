# Business logic for order
from app.core.database import db
from app.modules.orders.models import OrderModel
from bson.objectid import ObjectId

orders_collection = db["orders"]

async def create_order(order_data: OrderModel):
    order_dict = order_data.dict()
    result = await orders_collection.insert_one(order_dict)
    return str(result.inserted_id)

async def get_order_by_id(order_id: str):
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        order["id"] = str(order["_id"])
        return order
    return None

async def list_orders():
    orders_cursor = orders_collection.find()
    return [dict(order, id=str(order["_id"])) async for order in orders_cursor]

async def update_order_status(order_id: str, status: str):
    result = await orders_collection.update_one(
        {"_id": ObjectId(order_id)},
        {"$set": {"status": status}}
    )
    return result.modified_count > 0
