from pydantic import BaseModel, validator, ValidationError
from typing import Optional


class User(BaseModel):
    username: str
    password: int
    repeat_password: int
    phone: Optional[int]

    @validator("username")
    @classmethod
    def username_validation(cls, username: str) -> str:
        if len(username) < 4:
            raise ValueError('La longitud mínima es de 4 caracteres')
        if len(username) > 50:
            raise ValueError('La longitud máxima es de 50 caracteres')

        return username

    @validator("repeat_password")
    @classmethod
    def password_validation(cls, repeat_password: str, values: dict) -> str:
        if 'password' in values and repeat_password != values['password']:
            raise ValueError('La contraseñas son diferentes')

        return repeat_password


try:
    user = User(
        username='Luis',
        password=12,
        repeat_password=12
    )
    print(user.__dict__)
except ValidationError as e:
    print(e.json())
