from pydantic import BaseModel, validator
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res


class UserReviewRequestModel(BaseModel):
    user_id: int
    movie_id: int
    review: str
    score: float

    @validator('score')
    @classmethod
    def validate_score(cls, score: float) -> float:
        if score < 1:
            raise ValueError('El score debe ser mayor o igual a 1')
        if score > 5:
            raise ValueError('El score debe ser menor o igual a 5')

        return score


class UserReviewResponseModel(BaseModel):
    id: int
    movie_id: int
    review: str
    score: float

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
