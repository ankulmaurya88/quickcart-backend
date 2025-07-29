from fastapi import APIRouter

# Future modules (commented for now)
# from app.modules.products.routes import router as products_router
# from app.modules.cart.routes import router as cart_router
# from app.modules.orders.routes import router as orders_router

from app.modules.users.routes import router as users_router

api_router = APIRouter()

# Future route registrations (commented out for now)
# router.include_router(products_router, prefix="/products", tags=["Products"])
# router.include_router(cart_router, prefix="/cart", tags=["Cart"])
# router.include_router(orders_router, prefix="/orders", tags=["Orders"])

# Current auth/user routes
api_router.include_router(users_router, prefix="/auth", tags=["Auth"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])

