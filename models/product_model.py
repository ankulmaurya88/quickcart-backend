from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from app.utils.bson_objectid import PyObjectId

class Product(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
