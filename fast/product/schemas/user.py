from pydantic import BaseModel, validator


class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    @classmethod
    def validate_username(cls, username: str) -> str:
        if len(username) < 4:
            raise ValueError('El username debe tener mínimo 4 caracteres')
        if len(username) > 50:
            raise ValueError('El username debe tener máximo 50 caracteres')

        return username


class UserResponseModel(BaseModel):
    id: int
    username: str
