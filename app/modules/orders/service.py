# Business logic for order
from app.core.database import db
from app.modules.orders.schemas import OrderCreate, OrderUpdate
from app.modules.orders.schemas import OrderOut
from app.modules.orders.schemas import OrderList
from app.modules.orders.schemas import OrderStatusUpdate
from app.modules.orders.schemas import OrderModel
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
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

# async def list_orders():
#     orders_cursor = orders_collection.find()
#     return [dict(order, id=str(order["_id"])) async for order in orders_cursor]

# async def update_order_status(order_id: str, status: str):
#     result = await orders_collection.update_one(
#         {"_id": ObjectId(order_id)},
#         {"$set": {"status": status}}
#     )
#     return result.modified_count > 0

# async def update_order(order_id: str, order_data: OrderUpdate):
#     order_dict = order_data.dict(exclude_unset=True)
#     result = await orders_collection.update_one(
#         {"_id": ObjectId(order_id)},
#         {"$set": order_dict}
#     )
#     if result.modified_count > 0:
#         return await get_order_by_id(order_id)
#     return None     


# async def delete_order(order_id: str):
#     result = await orders_collection.delete_one({"_id": ObjectId(order_id)})
#     return result.deleted_count > 0     

# async def get_orders_by_user(user_id: str):
#     orders_cursor = orders_collection.find({"user_id": ObjectId(user_id)})
#     return [dict(order, id=str(order["_id"])) async for order in orders_cursor]
