from fastapi import FastAPI
from models import database, User, Movie, UserReview
from schemas import UserRequestModel, \
    MovieRequestModel, \
    UserReviewRequestModel, \
    UserResponseModel, \
    UserReviewResponseModel

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
    return UserResponseModel(id=user.id, username=user.username)


@app.post("/movies")
async def create_movie(movie: MovieRequestModel):
    movie = Movie.create(
        title=movie.title
    )
    return movie


@app.post("/reviews")
async def create_review(review: UserReviewRequestModel):
    review = UserReview.create(
        movie_id=review.movie_id,
        user_id=review.user_id,
        review=review.review,
        score=review.score
    )
    return UserReviewResponseModel(
        id=review.id,
        movie_id=review.movie_id,
        review=review.review,
        score=review.score
    )
