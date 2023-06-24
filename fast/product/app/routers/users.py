from ..models import User
from ..schemas import UserRequestModel, UserResponseModel
from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasicCredentials

router = APIRouter(prefix='/users')


@router.post("", response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )
    return user


@router.post("/login", response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials):
    password = User.create_password(credentials.password)
    user = User.select()\
        .where(User.username == credentials.username) \
        .where(User.password == password) \
        .first()

    if not user:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return user
