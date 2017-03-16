from connectdatabase import *
from peewee import *


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = ConnectDatabase.db


class School(BaseModel):
    pass
