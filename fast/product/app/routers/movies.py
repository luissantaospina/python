import functools
from typing import List
from ..schemas import MovieRequestModel, MovieResponseModel
from fastapi import APIRouter, Depends, Path, HTTPException, status
from ..helpers import oauth_schema
from ..services import MovieService
from ..repositories import MovieRepository

router = APIRouter(prefix='/movies')


def validate_movie(function):
    @functools.wraps(function)
    def wrapper(movie_id: int, token: str):
        movie = MovieRepository.get(movie_id)
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')

        return function(movie_id, token)

    return wrapper


@router.post("", response_model=MovieResponseModel, tags=["movies"])
async def create_movie(movie: MovieRequestModel, token: str = Depends(oauth_schema)) -> MovieResponseModel:
    movie_created = MovieService.create_movie(movie)
    return movie_created


@router.get("", response_model=List[MovieResponseModel], tags=["movies"])
async def get_movies(page: int = 1, limit: int = 10, token: str = Depends(oauth_schema)) \
        -> List[MovieResponseModel]:
    movies = MovieService.get_movies(page, limit)
    return [movie for movie in movies]


@router.get("/{movie_id}", response_model=MovieResponseModel, tags=["movies"])
@validate_movie
def get_movie(movie_id: int = Path(ge=1), token: str = Depends(oauth_schema)) -> MovieResponseModel:
    movie = MovieService.get_movie(movie_id)
    return movie


# TODO: Validate movie
@router.put("/{movie_id}", response_model=MovieResponseModel, tags=["movies"])
async def update_movie(movie_request: MovieRequestModel, movie_id: int = Path(ge=1),
                       token: str = Depends(oauth_schema)) -> MovieResponseModel:
    movie_updated = MovieService.update_movie(movie_request, movie_id)
    return movie_updated


@router.delete("/{movie_id}", response_model=MovieResponseModel, tags=["movies"])
@validate_movie
def delete_movie(movie_id: int = Path(ge=1), token: str = Depends(oauth_schema)) -> MovieResponseModel:
    movie_deleted = MovieService.delete_movie(movie_id)
    return movie_deleted
