from app.database import db
from bson import ObjectId
from datetime import datetime

async def create_order(user_id):
    cart = await db["carts"].find_one({"user_id": ObjectId(user_id)})
    if not cart or not cart["items"]:
        return {"error": "Cart is empty"}

    total = 0
    for item in cart["items"]:
        product = await db["products"].find_one({"_id": ObjectId(item["product_id"])})
        if product:
            total += product["price"] * item["quantity"]

    order_doc = {
        "user_id": ObjectId(user_id),
        "items": cart["items"],
        "total": total,
        "status": "placed",
        "created_at": datetime.utcnow()
    }
    await db["orders"].insert_one(order_doc)
    await db["carts"].delete_one({"user_id": ObjectId(user_id)})

    return {"message": "Order placed successfully", "total": total}

async def get_orders_by_user(user_id):
    orders = []
    cursor = db["orders"].find({"user_id": ObjectId(user_id)})
    async for order in cursor:
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders
