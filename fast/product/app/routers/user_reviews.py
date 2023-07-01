import functools
from typing import List
from ..models import UserReview
from ..schemas import UserReviewRequestModel, \
    UserReviewResponseModel, \
    UserReviewRequestPutModel
from fastapi import APIRouter, HTTPException, status, Depends, Path
from ..helpers import oauth_schema
from ..models import User
from ..helpers import get_current_user

router = APIRouter(prefix='/reviews')


def validate_review(function):
    @functools.wraps(function)
    def wrapper(review_id: int, token: str):
        review = UserReview.select().where(UserReview.id == review_id).first()
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

        return function(review_id, token)

    return wrapper


@router.post("", response_model=UserReviewResponseModel, tags=["reviews"])
async def create_review(review: UserReviewRequestModel, user: User = Depends(get_current_user)):
    review = UserReview.create(
        movie_id=review.movie_id,
        user_id=user.id,
        review=review.review,
        score=review.score
    )
    return review


@router.get("", response_model=List[UserReviewResponseModel], tags=["reviews"])
async def get_reviews(page: int = 1, limit: int = 10, token: str = Depends(oauth_schema)):
    reviews = UserReview.select().paginate(page, limit)
    return [review for review in reviews]


@router.get("/{review_id}", response_model=UserReviewResponseModel, tags=["reviews"])
@validate_review
def get_review(review_id: int = Path(ge=1), token: str = Depends(oauth_schema)):
    review = UserReview.select().where(UserReview.id == review_id).first()
    return review


@router.put("/{review_id}", response_model=UserReviewResponseModel, tags=["reviews"])
async def update_review(review_request: UserReviewRequestPutModel, review_id: int = Path(ge=1), token: str = Depends(oauth_schema)):
    review = UserReview.select().where(UserReview.id == review_id).first()
    review.review = review_request.review
    review.score = review_request.score
    review.save()
    return review


# with Path validate the route params
@router.delete("/{review_id}", response_model=UserReviewResponseModel, tags=["reviews"])
@validate_review
def delete_review(review_id: int = Path(ge=1), token: str = Depends(oauth_schema)):
    review = UserReview.select().where(UserReview.id == review_id).first()
    review.delete_instance()
    return review
