# This script can create the database tables based on your models
from models import *


class Build():

    @staticmethod
    def initialize_data():
        board1 = Board.create(board_name='first board')
        board2 = Board.create(board_name='second board')
        board3 = Board.create(board_name='third board')

        card1 = Card.create(title='első',
                            content="blabla",
                            status="to-do",
                            position=0,
                            assigned_board=1)
        card2 = Card.create(title='második',
                            content="semmi",
                            status="in_progress",
                            position=0,
                            assigned_board=1)
        card3 = Card.create(title='harmadik',
                            content="random",
                            status="done",
                            position=0,
                            assigned_board=1)
        card4 = Card.create(title='negyedik',
                            content="ezaz",
                            status="to-do",
                            position=0,
                            assigned_board=1)
        card5 = Card.create(title='ötödik',
                            content="fuck that",
                            status="review",
                            position=0,
                            assigned_board=1)
        card6 = Card.create(title='hatodik',
                            content="pls dont",
                            status="review",
                            position=0,
                            assigned_board=1)
