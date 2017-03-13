from peewee import *


class ConnectDatabase:

    def get_connect_string():
        try:
            with open('parameter.txt', "r") as db_name:
                return db_name.readline().strip()
        except:
            print("You need to create a database and store its name in a file named 'parameter.txt'. \
                  For more info, head over to the README")

    db = PostgresqlDatabase(get_connect_string())
