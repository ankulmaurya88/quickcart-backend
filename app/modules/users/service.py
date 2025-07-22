# Business logic for user
# users/service.py
from passlib.context import CryptContext
from bson import ObjectId
from pymongo.collection import Collection
from app.core.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def register_user(user_data, user_collection: Collection):
    user = user_collection.find_one({"email": user_data.email})
    if user:
        raise ValueError("User already exists")
    
    hashed = hash_password(user_data.password)
    result = user_collection.insert_one({
        "email": user_data.email,
        "hashed_password": hashed
    })
    token = create_access_token({"sub": str(user_data.email)})
    return {"email": user_data.email, "token": token}

def authenticate_user(user_data, user_collection: Collection):
    user = user_collection.find_one({"email": user_data.email})
    if not user or not verify_password(user_data.password, user["hashed_password"]):
        raise ValueError("Invalid credentials")
    
    token = create_access_token({"sub": str(user_data.email)})
    return {"email": user_data.email, "token": token}
