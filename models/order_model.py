from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId
from datetime import datetime
from app.utils.bson_objectid import PyObjectId

class OrderItem(BaseModel):
    product_id: PyObjectId
    quantity: int

class Order(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    items: List[OrderItem]
    total: float
    status: str = "placed"
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
