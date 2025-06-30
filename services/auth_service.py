from app.models.user_model import UserCreate
from app.database import db
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.config import JWT_SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(raw, hashed):
    return pwd_context.verify(raw, hashed)

async def register_user(data: UserCreate):
    existing = await db["users"].find_one({"email": data.email})
    if existing:
        return {"error": "User already exists"}
    
    hashed = hash_password(data.password)
    user_doc = {"email": data.email, "hashed_password": hashed, "role": "user"}
    result = await db["users"].insert_one(user_doc)
    return {"message": "User registered", "id": str(result.inserted_id)}

async def login_user(data: UserCreate):
    user = await db["users"].find_one({"email": data.email})
    if not user or not verify_password(data.password, user["hashed_password"]):
        return {"error": "Invalid credentials"}
    
    payload = {
        "id": str(user["_id"]),
        "email": user["email"],
        "role": user["role"],
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}
