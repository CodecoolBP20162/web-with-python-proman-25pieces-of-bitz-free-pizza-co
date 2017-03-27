from models import *
from connectdatabase import ConnectDatabase


class StateInit:

    def __init__(self, imp):
        self.__implementation = imp

    def change_state(self, state):
        self.__implementation = state

    def __getattr__(self, name):
        return getattr(self.__implementation, name)


class DatabaseLocalStorage:

    def init_db():
        pass


class DatabaseSQL:

    def init_db():
        ConnectDatabase.db.connect()
        ConnectDatabase.db.drop_tables([Board, Card], True, True)
        ConnectDatabase.db.create_tables([Board, Card], safe=True)
