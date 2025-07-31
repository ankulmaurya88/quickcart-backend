from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.database import connect_to_mongo, close_mongo_connection
from app.modules.products.routes import router as product_router
from app.modules.cart.routes import router as cart_router

app = FastAPI(
    title="QuickCart API",
    description="Backend for QuickCart E-commerce Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(product_router)
api_router.include_router(cart_router)