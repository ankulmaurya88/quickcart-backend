# FastAPI router for product
# modules/products/routes.py

from fastapi import APIRouter, HTTPException
from app.modules.products.schemas import ProductCreate, ProductOut
from app.modules.products.service import create_product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductOut)
async def add_product(product: ProductCreate):
    return await create_product(product)
