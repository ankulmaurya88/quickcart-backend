from fastapi import APIRouter, Depends
from app.models.product_model import Product
from app.services.product_service import create_product, get_all_products
from app.utils.jwt_handler import get_current_user

router = APIRouter()

@router.get("/")
async def list_products():
    return await get_all_products()

@router.post("/")
async def add_product(product: Product, user=Depends(get_current_user)):
    if user["role"] != "admin":
        return {"error": "Not authorized"}
    return await create_product(product)
