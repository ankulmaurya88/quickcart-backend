# Pydantic schemas for cart
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class CartItem(BaseModel):
    product_id: str
    quantity: int

class CartCreate(BaseModel):
    items: List[CartItem]

class CartOut(BaseModel):
    id: str
    user_id: str
    items: List[CartItem]
    total_price: float
