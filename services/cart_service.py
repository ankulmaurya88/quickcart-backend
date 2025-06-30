from app.database import db
from app.models.cart_model import CartItem
from bson import ObjectId

async def add_to_cart(user_id, item: CartItem):
    cart = await db["carts"].find_one({"user_id": ObjectId(user_id)})
    if not cart:
        cart_data = {"user_id": ObjectId(user_id), "items": [item.dict()]}
        await db["carts"].insert_one(cart_data)
    else:
        cart["items"].append(item.dict())
        await db["carts"].update_one(
            {"user_id": ObjectId(user_id)},
            {"$set": {"items": cart["items"]}}
        )
    return {"message": "Item added to cart"}

async def get_user_cart(user_id):
    cart = await db["carts"].find_one({"user_id": ObjectId(user_id)})
    if not cart:
        return {"items": []}
    cart["_id"] = str(cart["_id"])
    return cart
