# FastAPI router for cart
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_cart_collection
from app.modules.cart import service
from app.modules.cart.schemas import CartCreate, CartOut
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/", response_model=CartOut)
async def get_user_cart(user_id: str, db: AsyncIOMotorDatabase = Depends(get_cart_collection)):
    cart = await service.get_cart(db, user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.post("/", response_model=CartOut)
async def create_user_cart(user_id: str, cart: CartCreate, db: AsyncIOMotorDatabase = Depends(get_cart_collection)):
    return await service.create_cart(db, user_id, cart.items)

@router.put("/", response_model=CartOut)
async def update_user_cart(user_id: str, cart: CartCreate, db: AsyncIOMotorDatabase = Depends(get_cart_collection)):
    return await service.update_cart(db, user_id, cart.items)

@router.delete("/")
async def delete_user_cart(user_id: str, db: AsyncIOMotorDatabase = Depends(get_cart_collection)):
    result = await service.delete_cart(db, user_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cart not found")
    return {"message": "Cart deleted successfully"}
