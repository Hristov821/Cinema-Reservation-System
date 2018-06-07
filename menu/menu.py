from View.View import *


class menu():

    @classmethod
    def start(cls):
        View.clear()
        View.choice()
        choice = input('-> Type a choice : ')
        while True:
            if choice.lower() == 'print movies'or choice.lower() == '1':
                View.print_movies()
            if choice.lower() == 'movie projections'or choice.lower() == '2':
                View.print_projections_by_movie_name()

            if choice.lower() == 'login user' or choice.lower() == '3':
                View.login_user()

            if choice.lower() == 'register' or choice.lower() == '4':
                View.register_user()

            if choice.lower() == 'make reservation' or choice.lower() == '5':
                View.make_reservation()

            if choice.lower() == 'print movie projections by date' or choice.lower() == '6':
                View.print_movie_projections_by_date()

            if choice.lower() == 'help'or choice.lower() == '8':
                View.choice()
            if choice.lower() == 'finalize' or choice.lower() == '7':
                View.finalize()

            if choice.lower() == 'exit' or choice.lower() == '9':
                break
            if choice.lower() == 'clear' or choice.lower() == '10':
                View.clear()

            if choice.lower() == 'log out' or choice.lower() == '11':
                View.log_out()

            choice = input('-> Type choice ')


