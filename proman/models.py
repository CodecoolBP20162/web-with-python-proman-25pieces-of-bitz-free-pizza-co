from connectdatabase import *
from peewee import *


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = ConnectDatabase.db


class Board(BaseModel):
    board_name = CharField()


class Card(BaseModel):
    title = CharField()
    content = CharField()
    status = CharField()
    assigned_board = ForeignKeyField(Board)
    position = CharField()
