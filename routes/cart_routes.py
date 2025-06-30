from fastapi import APIRouter, Depends
from app.models.cart_model import CartItem
from app.services.cart_service import add_to_cart, get_user_cart
from app.utils.jwt_handler import get_current_user

router = APIRouter()

@router.post("/add")
async def add_item(item: CartItem, user=Depends(get_current_user)):
    return await add_to_cart(user["id"], item)

@router.get("/")
async def get_cart(user=Depends(get_current_user)):
    return await get_user_cart(user["id"])
