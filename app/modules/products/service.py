# Business logic for product
# modules/products/service.py

from app.modules.products.models import ProductModel
from app.modules.products.schemas import ProductCreate
# from app.core.database import db
from app.core.database import get_product_collection  # Assuming db setup
from bson import ObjectId

async def create_product(product_data: ProductCreate) -> ProductModel:
    product_dict = product_data.dict()
    result = await get_product_collection.insert_one(product_dict)
    product_dict["_id"] = result.inserted_id
    return ProductModel(**product_dict)

# async def get_product_by_id(product_id: str) -> ProductModel:
#     product = await get_product_collection.find_one({"_id": ObjectId(product_id)})
#     if not product:
#         raise ValueError("Product not found")
#     return ProductModel(**product)