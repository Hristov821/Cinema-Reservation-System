from ReservationControler import *
# from MovieControler import MovieControler
def start():
    UserControler.register_user('Ivan', 'PAROLA')
    UserControler.register_user('Ivan1', 'PAROLA')
    UserControler.register_user('Ivan2', 'PAROLA')
    UserControler.register_user('Ivan3', 'PAROLA')
    UserControler.register_user('Ivan4', 'PAROLA')
    MovieControler.create_movie('Burzi', 5.2)
    MovieControler.create_movie('Bavni', 2.3)

    ProjectionsControler.create_projection('2D', '2018-12-12', '12:30:00', 1)
    ProjectionsControler.create_projection('2D', '2018-12-12', '15:30:00', 2)

    ReservationControler.create_reservation(1, 1, 1, 1)
    ReservationControler.create_reservation(1, 1, 2, 2)
    ReservationControler.create_reservation(1, 1, 3, 3)
    ProjectionsControler.create_projection('2D', '2014-12-12', '15:30:00', 2)


start()