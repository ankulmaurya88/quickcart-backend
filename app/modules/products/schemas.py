# Pydantic schemas for product
# modules/products/schemas.py

from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ProductOut(ProductCreate):
    id: str
