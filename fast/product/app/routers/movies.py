from ..schemas import MovieRequestModel, MovieResponseModel
from fastapi import APIRouter, Depends
from ..helpers import oauth_schema
from ..services import MovieService

router = APIRouter(prefix='/movies')


@router.post("", response_model=MovieResponseModel, tags=["movies"])
async def create_movie(movie: MovieRequestModel, token: str = Depends(oauth_schema)) -> MovieResponseModel:
    movie_created = MovieService.create_movie(movie)
    return movie_created
