from pydantic import BaseModel


class MovieRequestModel(BaseModel):
    title: str


class MovieResponseModel(BaseModel):
    title: str
