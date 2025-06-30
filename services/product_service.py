from app.database import db
from app.models.product_model import Product

async def create_product(product: Product):
    product_dict = product.dict(by_alias=True)
    result = await db["products"].insert_one(product_dict)
    return {"id": str(result.inserted_id), "message": "Product added"}

async def get_all_products():
    products = []
    cursor = db["products"].find()
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        products.append(doc)
    return products
