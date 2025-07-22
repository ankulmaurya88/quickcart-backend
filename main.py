from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.modules.users.routes import router as users_router  # optional, if you have user auth
from app.api.routes import router
from app.api.routes import api_router  # Import the API router
from core.config import settings
from core.database import connect_to_mongo, close_mongo_connection

app1 = FastAPI(
    title="QuickCart API",
    description="Backend for QuickCart E-commerce Platform",
    version="1.0.0"
)

# Allow CORS
app1.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app1.include_router(api_router)
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to QuickCart API!"}
# MongoDB connection handlers
@app1.on_event("startup")
async def startup_db():
    await connect_to_mongo()

@app1.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()
