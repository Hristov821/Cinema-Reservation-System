from CreateDatabase.CreateDatabase import *
from .UserControler import UserControler
from .ProjectionsControler import ProjectionsControler


class ReservationControler():
    session = session

    @classmethod
    def seat_is_taken(cls, row, col):
        try:
            session.query(Reservations).filter(Reservations.row == row).\
                filter(Reservations.col == col).\
                filter(Reservations.user_id is not None).one()
            return True
        except:
            return False

    @classmethod
    def taken_seets(cls, projection_id):
        if ProjectionsControler.get_projection_by_id(projection_id) is None:
            raise ValueError('Projection dont exist')
        return session.query(Reservations.row, Reservations.col).\
            filter(Reservations.projection_id == projection_id)\
            .all()

    @classmethod
    def create_reservation(cls, user_id, projection_id, row, col):
        if UserControler.get_user_by_id(user_id) is None:
            raise ValueError('User dont exist')

        if ProjectionsControler.get_projection_by_id(projection_id) is None:
            raise ValueError('Projection dont exist')

        if ReservationControler.seat_is_taken(row, col) is True:
            raise ValueError('Seat is taken')

        if row > 10 or row < 1:
            raise ValueError('row must be between 1 - 10')

        if col < 1 or col > 10:
            raise ValueError('col must be between 1 - 10 ')

        session.add(Reservations(user_id=user_id,
                                 projection_id=projection_id,
                                 row=row, col=col))
#       session.commit()
        
