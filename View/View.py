from Controlers.MovieControler import *
from Controlers.ProjectionsControler import *
from Controlers.ReservationControler import *
from Controlers.UserControler import *
from prettytable import PrettyTable
from .UserState import UserState
import os
import getpass


class View():

    @classmethod
    def clear(cls):
        os.system('cls||clear')

    @classmethod
    def choice(cls):
        print('[1]Print movies')
        print('[2]Movie projections')
        print('[3]Login user')
        print('[4]Register')
        print('[5]Make reservation')
        print('[6]Print movie projections by date')
        print('[7]Finalize')
        print('[8]Help')
        print('[9]Exit')
        print('[10]Clear')
        print('[11]log out')

    @classmethod
    def print_movies(cls):
        table = PrettyTable(["ID", "Movie Name", "Rating"])
        for i in MovieControler.get_movies():
            table.add_row([i.id, i.name, i.rating])
        print(table)

    @classmethod
    def print_projection_room(cls, projection_id):
        try:
            free_seets = ReservationControler.taken_seets(projection_id)
        except ValueError as e:
            print(e)
            return
        for i in range(1, 11):
            for j in range(1, 11):
                if (i, j) in free_seets:
                    print('X ', end='')
                else:
                    print('. ', end='')
            print()

    @classmethod
    def print_projections(cls):
        table = PrettyTable(['ID', 'Movie', 'Date', 'Time'])
        for i in ProjectionsControler.get_all_projections():
            table.add_row([i.id, i.movie, i.to_date(), i.to_time()])
        print(table)

    @classmethod
    def print_projections_by_movie_name(cls):
        flag = False
        while flag is False:
            movie = input('-> Movie ')
            projections = ProjectionsControler.get_movie_projections(movie)
            if len(projections) == 0:
                print('No projections for {}'.format(movie))
            else:
                flag = True
        table = PrettyTable(['ID', 'Movie', 'Date', 'Time'])
        for i in projections:
            table.add_row([i.id, i.movie, i.to_date(), i.to_time()])
        print(table)

    @classmethod
    def login_user(cls):
        if UserState.user_loged == True:
            print('You already logged')
            return True
        username = input('->Username : ')
        password = getpass.getpass('->Password :')
        while UserControler.login_user(username, password) is False:
            choice = input('Wrong username or password try again ? - Y/N ')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                username = input('->Username : ')
                password = getpass.getpass('->Password :')
            if choice.lower() == 'n' or choice.lower() == 'n':
                return False
            else:
                print('Invalid command')
        UserState.User = UserControler.get_user_by_name(username)
        UserState.user_loged = True
        return True

    @classmethod
    def register_user(cls):
        username = input('->Username : ')
        password = getpass.getpass('->Password :')
        state = True
        while state:
            try:
                UserControler.register_user(username, password)

                UserState.user_loged = True
                UserState.user = UserControler.get_user_by_name(username)
                print('Sucsfuly registered {}'.format(UserState.user.username))
                return True
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)
            while True:
                choice = input('Continiue Y/N ')
                if choice.lower() == 'n' or choice.lower() =='no':
                    state = False
                    break
                elif choice.lower() == 'y' or choice.lower() == 'yes':
                    username = input('->Username : ')
                    password = getpass.getpass('->Password :')
                    break
                else:
                    print('Not valid command')
                    choice = input('Choice ')

    @classmethod
    def make_reservation(cls):
        session.rollback()
        if UserState.user_loged is False:
            print('U are not logged do u wanna log or register')
            choice = input('Register/log in/stop - >')
            while UserState.user_loged is False:
                if choice.lower() == 'register':
                    cls.register_user()
                    break
                if choice.lower() == 'log in':
                    cls.login_user()
                    break
                if choice.lower() == 'stop':
                    break
                else:
                    print('invalid command')
                    choice = input('->register/log in/stop - ')
        if UserState.user_loged is True:
            projection_id = input('->projection  ')
            num_tikets = int(input('->number of tickets '))
            cls.print_projection_room(projection_id)
            if num_tikets > 100 - len(ReservationControler.taken_seets(projection_id)):
                print('Not enough free seets')
                return

            for i in range(num_tikets):
                cls.make_simple_reservation(
                    projection_id, UserState.user.id)
            print('if u want to save your reservation type {} or {} '.format('finalize', 7))

    @classmethod
    def make_simple_reservation(cls, projection_id, user_id):
        flag = False
        while flag is False:
            try:
                row = int(input('-> row '))
                col = int(input('-> col '))
                ReservationControler.create_reservation(
                    user_id, projection_id, row, col)
                flag = True
                cls.print_projection_room(projection_id)
            except ValueError as e:
                print(str(e))
            except Exception as e:
                print(str(e))

    @classmethod
    def print_movie_projections_by_date(cls):
        state = True
        while state:
            try:
                movie = input('->Movie ')
                date = input('-> Date')
                projections = ProjectionsControler.get_movie_projections_by_date(
                    movie, date)
                if len(projections) > 0:
                    table = PrettyTable(['Movie', 'Date', 'Time'])
                    for i in projections:
                        table.add_row([i.movie, i.to_date(), i.to_time()])
                    print(table)
                else:
                    print('No projections for this movie or date')
                state = False
            except ValueError as e:
                print(e)
                print('-> try again ? Y/N' )
                choice = input('-> Choice ')
                while choice.lower() != 'y' or choice.lower() != 'yes'or choice.lower() != 'n' or choice.lower() != 'no':
                    if choice.lower() == 'y' or choice.lower() == 'yes':
                        print('-> Type again')
                        break
                    elif choice.lower() == 'n' or choice.lower() == 'no':
                        state = False
                        break
                    else:
                        print('Not command')
                    choice = input('-> Choice ')

    @classmethod
    def log_out(cls):
        if UserState.user_loged is False:
            print('U are not logged')
        else:
            UserState.user_loged = False
            UserState.user = None
            print('Sucsfuly log out')

    @classmethod
    def finalize(cls):
        session.commit()
