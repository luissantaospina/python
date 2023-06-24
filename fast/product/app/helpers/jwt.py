import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = 'HFDA6**FYGHJga7G67DSIAY'
oauth_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')


def create_access_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }

    return jwt.encode(data, SECRET_KEY, algorithm="HS256")
