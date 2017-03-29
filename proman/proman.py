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
    return render_template("boardlist.html")


@app.route('/detailed_view')
def detailed_view():
    new = Card.select().where(Card.status == "new")
    in_progress = Card.select().where(Card.status == "in_progress")
    done = Card.select().where(Card.status == "done")
    review = Card.select().where(Card.status == "review")
    return render_template("columns.html", new=new, in_progress=in_progress, done=done, review=review)


@app.route("/update/<card_id>/<card_title>/<card_textarea>")
def update_card(card_id, card_title, card_textarea):
    updated_card = Card.update(title=card_title,
                               content=card_textarea).where(Card.id == card_id)
    updated_card.execute()

    return jsonify(card_title, card_textarea)


if __name__ == '__main__':
    current_state = state.StateInit(state.DatabaseSQL)
    # current_state.change_state(state.DarabaseLocalStorage)
    current_state.init_db()
    Build.initialize_data()
    app.run(debug=True)
