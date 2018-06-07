
from .MovieControler import *

class ProjectionsControler():
    session = session

    @classmethod
    def get_projection_by_id(cls, id):
        try:
            return session.query(Projections).\
                filter(Projections.id == id).one()
        except:
            return None

    # @classmethod
    # def projection_exist(cls, type, date, time, movie_id):
    #     try:
    #         count = len(session.query(Projections).filter(Projections.type == type,
    #                                                       Projections.date == cls.date_setter(
    #                                                           date),
    #                                                       Projections.time == cls.time_setter(
    #                                                           time),
    #                                                       Projections.movie_id == movie_id).all())
    #         return True
    #     except:
    #         return False

    @classmethod
    def get_all_projections(cls):
        return session.query(Projections).\
            order_by(Projections.date).\
            order_by(Projections.time).all()

    @classmethod
    def get_movie_projections(cls, movie):
        return session.query(Projections).\
            filter(Movies.name == movie).\
            filter(Movies.id == Projections.movie_id).\
            order_by(Projections.date, Projections.time).all()

    @classmethod
    def date_validator(cls, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @classmethod
    def date_setter(cls, date):
        a = datetime.strptime(date, '%Y-%m-%d')
        b = datetime(1970, 1, 1)
        return int((a - b).total_seconds())

    @classmethod
    def time_setter(cls, time):
        ftr = [3600, 60, 1]
        return sum(
            [a * b for a, b in zip(ftr, map(int, time.split(':')))])

    @classmethod
    def create_projection(cls, type, date, time, movie_id):
        session.add(Projections(type=type, date=cls.date_setter(date),
                                time=cls.time_setter(time), movie_id=movie_id))
        session.commit()

    @classmethod
    def get_movie_projections_by_date(cls, movie, date):
        if type(date) is not str:
            raise ValueError('date must be string')
        if type(movie) is not str:
            raise ValueError('movie must be string')
        if cls.date_validator(date) is False:
            raise ValueError('date format must be Y-m-d')
        if MovieControler.movie_exist(movie) is False:
            raise ValueError('Movie dont exist')
        date = cls.date_setter(date)
        return session.query(Projections).\
            filter(Movies.name == movie).\
            filter(Movies.id == Projections.movie_id).\
            filter(Projections.date == date).\
            order_by(Projections.date, Projections.time).all()
