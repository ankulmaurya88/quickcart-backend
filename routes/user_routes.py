from fastapi import APIRouter, Depends, HTTPException
from app.models.user_model import UserCreate
from app.services.auth_service import register_user, login_user

router = APIRouter()

@router.post("/register")
async def register(data: UserCreate):
    return await register_user(data)

@router.post("/login")
async def login(data: UserCreate):  # Reuse model or create LoginSchema
    return await login_user(data)
