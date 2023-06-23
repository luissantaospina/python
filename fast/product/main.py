from fastapi import FastAPI
from typing import List
from models import database, User, Movie, UserReview
from schemas import UserRequestModel, \
    MovieRequestModel, \
    UserReviewRequestModel, \
    UserResponseModel, \
    UserReviewResponseModel, \
    MovieResponseModel

app = FastAPI()


@app.on_event('startup')
def startup():
    if database.is_closed():
        database.connect()
    database.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not database.is_closed():
        database.close()


@app.post("/users", response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )
    return user


@app.post("/movies", response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    movie = Movie.create(
        title=movie.title
    )
    return movie


@app.post("/reviews", response_model=UserReviewResponseModel)
async def create_review(review: UserReviewRequestModel):
    review = UserReview.create(
        movie_id=review.movie_id,
        user_id=review.user_id,
        review=review.review,
        score=review.score
    )
    return review


@app.get("/reviews", response_model=List[UserReviewResponseModel])
async def get_reviews():
    reviews = UserReview.select()
    return [review for review in reviews]


@app.get("/reviews/{review_id}", response_model=UserReviewResponseModel)
async def get_review(review_id: int):
    review = UserReview.select().where(UserReview.id == review_id).first()
    return review
