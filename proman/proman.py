import os
import state
from build import Build
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app, jsonify

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'proman.db'),
    SECRET_KEY='Sm9obiBTY2hyb20ga2lja3MgYXNz'))


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route('/')
def display_homepage():
    board_names_from_db = Board.select().where(Board.id > 0)
    return render_template("boardlist.html", board_names_from_db=board_names_from_db)


@app.route('/update_board/<board_id>/<newname>')
def update_board(board_id, newname):
    updated_board = Board.update(board_name=newname).where(Board.id == board_id)
    updated_board.execute()
    return jsonify(newname)


@app.route('/detailed_view')
def detailed_view():
    new1 = Card.select().where(Card.status == "to-do", Card.assigned_board == 1)
    in_progress1 = Card.select().where(Card.status == "in_progress", Card.assigned_board == 1)
    done1 = Card.select().where(Card.status == "done", Card.assigned_board == 1)
    review1 = Card.select().where(Card.status == "review", Card.assigned_board == 1)

    new2 = Card.select().where(Card.status == "to-do", Card.assigned_board == 2)
    in_progress2 = Card.select().where(Card.status == "in_progress", Card.assigned_board == 2)
    done2 = Card.select().where(Card.status == "done", Card.assigned_board == 2)
    review2 = Card.select().where(Card.status == "review", Card.assigned_board == 2)

    new3 = Card.select().where(Card.status == "to-do", Card.assigned_board == 3)
    in_progress3 = Card.select().where(Card.status == "in_progress", Card.assigned_board == 3)
    done3 = Card.select().where(Card.status == "done", Card.assigned_board == 3)
    review3 = Card.select().where(Card.status == "review", Card.assigned_board == 3)

    return render_template("index.html", new1=new1, new2=new2, new3=new3, in_progress1=in_progress1,
                           in_progress2=in_progress2, in_progress3=in_progress3, done1=done1, done2=done2, done3=done3,
                           review1=review1, review2=review2, review3=review3)


@app.route("/highest_id/<assigned_board>")
def get_highest_id(assigned_board):
    board = Board.select(Board.highest_id).where(Board.id == assigned_board).get()

    return jsonify(board.highest_id)


@app.route("/new/<card_id>/<card_status>/<assigned_board>")
def new_card(card_id, card_status, assigned_board):
    new_card = Card.create(title=None,
                           content=None,
                           status=card_status,
                           position=0,
                           assigned_board=assigned_board)
    id = card_id.replace("card", "")
    board = Board.update(highest_id=int(id)).where(Board.id == assigned_board)
    board.execute()

    return jsonify("card added successfully")


@app.route("/update/<card_id>/<card_title>/<card_textarea>/<card_status>")
def update_card(card_id, card_title, card_textarea, card_status):
    updated_card = Card.update(title=card_title,
                               content=card_textarea,
                               status=card_status).where(Card.id == card_id)
    updated_card.execute()

    return jsonify(card_title, card_textarea)


@app.route("/update_card_position/<card_id>/<board_id>/<card_status>")
def update_card_position(card_id, board_id, card_status):
    updated_card = Card.update(status=card_status).where(Card.id == card_id)
    updated_card.execute()

    return jsonify(card_status, board_id)


@app.route("/delete/<card_id>")
def delete(card_id):
    delete_card = Card.delete().where(Card.id == card_id)
    delete_card.execute()

    return jsonify("successfully deleted card")


if __name__ == '__main__':
    current_state = state.StateInit(state.DatabaseSQL)
    # current_state.change_state(state.DarabaseLocalStorage)
    current_state.init_db()
    Build.initialize_data()
    app.run(debug=True)
