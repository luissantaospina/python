import jwt
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from ..models.user import User

SECRET_KEY = 'HFDA6**FYGHJga7G67DSIAY'
oauth_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')


def create_access_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }

    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


def decode_token(token: str = Depends(oauth_schema)):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_current_user(token: str = Depends(oauth_schema)) -> User:
    data = decode_token(token)
    return User.select().where(User.id == data['user_id']).first()
