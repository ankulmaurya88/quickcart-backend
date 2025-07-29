from app.core.database import db
from app.modules.users.models import UserModel
from app.modules.users.schemas import UserCreate
from app.core.security import hash_password, verify_password
from bson import ObjectId

user_collection = db.get_collection("users")

async def create_user(user_data: UserCreate) -> UserModel:
    print("came here somehow")
    user_dict = user_data.dict()
    user_dict["hashed_password"] = hash_password(user_dict.pop("password"))
    user_dict["is_active"] = True
    user_dict["is_admin"] = False

    result = await user_collection.insert_one(user_dict)
    user_dict["_id"] = result.inserted_id

    return UserModel(**user_dict)


async def get_user_by_email(email: str) -> UserModel:
    user = await user_collection.find_one({"email": email})
    if user:
        return UserModel(**user)
    return None

async def authenticate_user(email: str, password: str) -> UserModel:
    user = await get_user_by_email(email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
