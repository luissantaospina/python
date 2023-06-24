from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from .models import database, User, Movie, UserReview
from .routers import user_router, movie_router, user_review_router
from fastapi.security import OAuth2PasswordRequestForm
from .helpers import create_access_token

app = FastAPI()
api_v1 = APIRouter(prefix='/api/v1')
api_v1.include_router(user_router)
api_v1.include_router(user_review_router)
api_v1.include_router(movie_router)


@api_v1.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')
    return {'access_token': create_access_token(user), 'token_type': 'Bearer'}

app.include_router(api_v1)


@app.on_event('startup')
def startup():
    if database.is_closed():
        database.connect()
    database.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not database.is_closed():
        database.close()
