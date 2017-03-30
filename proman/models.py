from connectdatabase import *
from peewee import *


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = ConnectDatabase.db


class Board(BaseModel):
    board_name = CharField()
    highest_id = IntegerField(default=0)


class Card(BaseModel):
    title = CharField(null=True)
    content = CharField(null=True)
    status = CharField()
    position = IntegerField()
    assigned_board = ForeignKeyField(Board)
