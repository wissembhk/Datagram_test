from fastapi import APIRouter
from services.userService import create_user
from models.schemas import UserSchema
router = APIRouter(prefix="/user")


@router.post('/user')
async def create_userr(user: UserSchema):
    return await create_user(user)
