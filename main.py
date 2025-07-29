from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.database import connect_to_mongo, close_mongo_connection

app1 = FastAPI(
    title="QuickCart API",
    description="Backend for QuickCart E-commerce Platform",
    version="1.0.0"
)

app1.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app1.include_router(api_router)

