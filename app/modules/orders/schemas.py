# Pydantic schemas for order
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]
    total_price: float

class OrderResponse(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    total_price: float
    status: str
    created_at: datetime
