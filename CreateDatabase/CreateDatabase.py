from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, Time
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)

    def __repr__(self):
        return self.username


class Movies(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)

    def __str__(self):
        return '{}'.format(self.name)

    def formated(self):
        return '[{}]-{} ({})'.format(self.id, self.name, self.rating)


class Projections(Base):
    __tablename__ = "Projections"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    date = Column(Integer)
    time = Column(Integer)
    movie_id = Column(Integer, ForeignKey("Movies.id"))
    movie = relationship(Movies, backref="Projections")

    def __str__(self):
        return '[{}] -{} {} {}'.\
            format(self.id, self.movie, self.to_date(), self.to_time())

    def to_date(self):
        return datetime.fromtimestamp(self.date).strftime("%Y-%m-%d")

    def to_time(self):
        # return datetime.fromtimestamp(self.time).strftime("%h-%m-%s")
        m, s = divmod(self.time, 60)
        h, m = divmod(m, 60)
        return '{}:{}:{}'.format(h, m, s)


class Reservations(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"), default=None)
    projection_id = Column(Integer, ForeignKey('Projections.id'))
    user = relationship(Users, backref="Reservations")
    row = Column(Integer, default=None)
    col = Column(Integer, default=None)

    def __repr__(self):
        return '[{}] {} {}'.format(self.projection_id, self.row, self.col)




engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
