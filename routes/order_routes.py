from fastapi import APIRouter, Depends
from app.services.order_service import create_order, get_orders_by_user
from app.utils.jwt_handler import get_current_user

router = APIRouter()

@router.post("/create")
async def place_order(user=Depends(get_current_user)):
    return await create_order(user["id"])

@router.get("/")
async def order_history(user=Depends(get_current_user)):
    return await get_orders_by_user(user["id"])
