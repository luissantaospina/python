from ..models import User
from ..schemas import UserRequestModel, UserResponseModel


class UserService:
    @classmethod
    def create_user(cls, user: UserRequestModel) -> UserResponseModel:
        hash_password = User.create_password(user.password)
        user = User.create(
            username=user.username,
            password=hash_password
        )
        return user
