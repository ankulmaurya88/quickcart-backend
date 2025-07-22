# FastAPI router for order
from fastapi import APIRouter, HTTPException, Depends
from app.modules.orders.schemas import OrderCreate, OrderResponse
from app.modules.orders.models import OrderModel
from app.modules.orders.service import create_order, get_order_by_id, list_orders, update_order_status
from app.core.auth import verify_token

router = APIRouter()

@router.post("/", response_model=dict)
async def place_order(order: OrderCreate, user=Depends(verify_token)):
    order_model = OrderModel(**order.dict())
    order_id = await create_order(order_model)
    return {"message": "Order placed successfully", "order_id": order_id}

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str, user=Depends(verify_token)):
    order = await get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/", response_model=list[OrderResponse])
async def get_all_orders(user=Depends(verify_token)):
    return await list_orders()

@router.patch("/{order_id}", response_model=dict)
async def update_status(order_id: str, status: str, user=Depends(verify_token)):
    success = await update_order_status(order_id, status)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found or not updated")
    return {"message": "Order status updated"}
