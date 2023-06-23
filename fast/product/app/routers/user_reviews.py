from typing import List
from ..models import UserReview
from ..schemas import UserReviewRequestModel, \
    UserReviewResponseModel, \
    UserReviewRequestPutModel
from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/reviews')


@router.post("", response_model=UserReviewResponseModel)
async def create_review(review: UserReviewRequestModel):
    review = UserReview.create(
        movie_id=review.movie_id,
        user_id=review.user_id,
        review=review.review,
        score=review.score
    )
    return review


@router.get("", response_model=List[UserReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10):
    reviews = UserReview.select().paginate(page, limit)
    return [review for review in reviews]


@router.get("/{review_id}", response_model=UserReviewResponseModel)
async def get_review(review_id: int):
    review = UserReview.select().where(UserReview.id == review_id).first()
    return review


@router.put("/{review_id}", response_model=UserReviewResponseModel)
async def update_review(review_id: int, review_request: UserReviewRequestPutModel):
    review = UserReview.select().where(UserReview.id == review_id).first()
    review.review = review_request.review
    review.score = review_request.score
    review.save()
    return review


@router.delete("/{review_id}", response_model=UserReviewResponseModel)
async def delete_review(review_id: int):
    review = UserReview.select().where(UserReview.id == review_id).first()
    review.delete_instance()
    return review
