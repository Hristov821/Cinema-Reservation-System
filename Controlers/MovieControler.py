from CreateDatabase.CreateDatabase import *


class MovieControler():
    @classmethod
    def get_movie(cls, movie_name):
        if cls.movie_exist(movie_name) is False:
            raise ValueError('Movie doesnt Exist')
        return session.query(Movies).filter(Movies.name == movie_name).all()

    @classmethod
    def get_movies(cls):
        return session.query(Movies).all()
        
    @classmethod
    def create_movie(cls, movie_name, rating):
        if cls.movie_exist(movie_name) is True:
            raise ValueError('Movie Exist')
        if rating > 10 or rating < 1:
            raise ValueError('Invalid value for rating')
        session.add(Movies(name=movie_name, rating=rating))

    @classmethod
    def movie_exist(cls, movie_name):
        count = session.query(Movies.name).filter(
            Movies.name == movie_name).count()
        if count == 0:
            return False
        return True


