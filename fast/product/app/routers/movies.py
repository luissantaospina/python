from ..models import Movie
from ..schemas import MovieRequestModel, MovieResponseModel
from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/movies')


@router.post("", response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    movie = Movie.create(
        title=movie.title
    )
    return movie
