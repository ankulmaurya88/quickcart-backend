from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId
from app.utils.bson_objectid import PyObjectId

class UserBase(BaseModel):
    email: EmailStr
    role: str = "user"

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    hashed_password: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
