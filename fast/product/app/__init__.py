from fastapi import FastAPI
from .models import database, User, Movie, UserReview
from .schemas import UserRequestModel, \
    MovieRequestModel, \
    UserReviewRequestModel, \
    UserResponseModel, \
    UserReviewResponseModel, \
    MovieResponseModel, \
    UserReviewRequestPutModel
from .routers import user_router, movie_router, user_review_router

app = FastAPI()
app.include_router(user_router)
app.include_router(user_review_router)
app.include_router(movie_router)


@app.on_event('startup')
def startup():
    if database.is_closed():
        database.connect()
    database.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not database.is_closed():
        database.close()
