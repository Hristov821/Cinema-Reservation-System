from CreateDatabase.CreateDatabase import *
import hashlib
import crypt


class UserControler():
    session = session

    @classmethod
    def get_user_by_id(cls, id):
        try:
            return session.query(Users).filter(Users.id == id).one()
        except Exception as e :
            return None

    @classmethod
    def get_user_by_name(cls, username):
        try:
            user = session.query(Users)\
                .filter(Users.username == username).one()
            return user
        except Exception as e:
            return None

    @classmethod
    def generete_salt(self):
        return crypt.mksalt(crypt.METHOD_SHA256)

    @classmethod
    def hash_password(cls, password, salt):
        ps = password + salt
        return hashlib.sha256(ps.encode('utf-8')).hexdigest()

    @classmethod
    def register_user(cls, username, password):
        if type(username) is not str:
            raise TypeError('Username must be string')
        if type(password) is not str:
            raise TypeError('password must be string')
        if cls.get_user_by_name(username) is not None:
            raise ValueError('User Exsit')
        salt = cls.generete_salt()
        pas = cls.hash_password(password, salt)
        session.add(Users(username=username, password=pas, salt=salt))
        session.commit()
        return True

    @classmethod
    def login_user(cls, username, password):
        if cls.get_user_by_name(username) is None:
            return False
        user = cls.get_user_by_name(username)
        return cls.hash_password(password, user.salt) == user.password

