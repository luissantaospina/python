from ..models import Movie
from ..schemas import MovieRequestModel, MovieResponseModel


class MovieService:

    @classmethod
    def create_movie(cls, movie: MovieRequestModel) -> MovieResponseModel:
        movie = Movie.create(title=movie.title)
        return movie
