from fastapi import FastAPI
from app.routes import user_routes, product_routes, cart_routes, order_routes
from app.middleware.error_handler import CustomExceptionMiddleware

app = FastAPI(title="QuickCart API")
app.add_middleware(CustomExceptionMiddleware)
# Include routers
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(cart_routes.router, prefix="/cart", tags=["Cart"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
