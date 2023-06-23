from ..models import User
from ..schemas import UserRequestModel, UserResponseModel
from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/users')


@router.post("", response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )
    return user
