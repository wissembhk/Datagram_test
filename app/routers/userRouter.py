from fastapi import APIRouter
from services.userService import create_user
from models.schemas import UserSchema
router = APIRouter(prefix="/user")


@router.post('/add')
async def create_user_router(user: UserSchema):
    return await create_user(user)
