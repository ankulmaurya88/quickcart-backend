from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from app.utils.bson_objectid import PyObjectId

class CartItem(BaseModel):
    product_id: PyObjectId
    quantity: int

class Cart(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    items: List[CartItem] = []

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
