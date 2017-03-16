import os
from peewee import *
from connectdatabase import ConnectDatabase
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'proman.db'),
    SECRET_KEY='Sm9obiBTY2hyb20ga2lja3MgYXNz'))


def init_db():
    ConnectDatabase.db.connect()
    # ConnectDatabase.db.drop_tables([Applicant, School, City, Mentor, InterviewSlot,
    #                                 Interview, Question, Email], True, True)
    # ConnectDatabase.db.create_tables([Applicant, School, City, Mentor, InterviewSlot,
    #                                   Interview, Question, Email], safe=True)


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
    return render_template("columns.html")


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
