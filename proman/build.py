# This script can create the database tables based on your models
from models import *


class Build():

    @staticmethod
    def initialize_data():
        # Schools
        board1 = Board.create(board_name='first board')
        board2 = Board.create(board_name='second board')
        board3 = Board.create(board_name='third board')

        # card1 = Card.create(school_name='Codecool Budapest')
        # card2 = Card.create(school_name='Codecool Miskolc')
        # card3 = Card.create(school_name='Codecool Kraków')
