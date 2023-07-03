from ..models import UserReview
from ..schemas import UserReviewRequestModel, UserReviewRequestPutModel, UserReviewResponseModel
from fastapi import Path
from ..models import User
from typing import List


class UserReviewService:

    @classmethod
    def create_review(cls, review: UserReviewRequestModel, user: User) -> UserReviewResponseModel:
        review = UserReview.create(
            movie_id=review.movie_id,
            user_id=user.id,
            review=review.review,
            score=review.score
        )
        return review

    @classmethod
    def get_reviews(cls, page: int = 1, limit: int = 10) -> List[UserReviewResponseModel]:
        reviews = UserReview.select().paginate(page, limit)
        return [review for review in reviews]

    @classmethod
    def get_review(cls, review_id: int = Path(ge=1)) -> UserReviewResponseModel:
        review = UserReview.select().where(UserReview.id == review_id).first()
        return review

    @classmethod
    def update_review(cls, review_request: UserReviewRequestPutModel, review_id: int = Path(ge=1))\
            -> UserReviewResponseModel:
        review = UserReview.select().where(UserReview.id == review_id).first()
        review.review = review_request.review
        review.score = review_request.score
        review.save()
        return review

    @classmethod
    def delete_review(cls, review_id: int = Path(ge=1)) -> UserReviewResponseModel:
        review = UserReview.select().where(UserReview.id == review_id).first()
        review.delete_instance()
        return review
