from fastapi import APIRouter, HTTPException, Depends
from app.modules.users import schemas, service
from app.core.database import get_user_collection
from pymongo.collection import Collection

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=schemas.UserResponse)
async def register(user: schemas.UserCreate, user_collection: Collection = Depends(get_user_collection)):
    try:
        return await service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=schemas.UserResponse)
def login(user: schemas.UserLogin, user_collection: Collection = Depends(get_user_collection)):
    try:
        return service.authenticate_user(user, user_collection)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
