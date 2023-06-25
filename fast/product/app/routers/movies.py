from ..models import Movie
from ..schemas import MovieRequestModel, MovieResponseModel
from fastapi import APIRouter, Depends
from ..helpers import oauth_schema

router = APIRouter(prefix='/movies')


@router.post("", response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel, token: str = Depends(oauth_schema)):
    movie = Movie.create(
        title=movie.title
    )
    return movie
