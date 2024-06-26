import sqlite3
import click
from flask import current_app, g


# The close_db and init_db_command functions 
# need to be registered with the application instance.
# otherwise, they won’t be used by the application. 
# Since you’re using a factory function, that instance 
# isn’t available when writing the functions. Instead, 
# write a function that takes an application and 
# does the registration.
def init_app(app):
    # tells Flask to call that function when 
    # cleaning up after returning the response.
    app.teardown_appcontext(close_db)

    # adds a new command that can be called with the flask command.
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# The close_db and init_db_command functions 
# need to be registered with the application instance.
# otherwise, they won’t be used by the application. 
# Since you’re using a factory function, that instance 
# isn’t available when writing the functions. Instead, 
# write a function that takes an application and 
# does the registration.
def init_app(app):
    # tells Flask to call that function when 
    # cleaning up after returning the response.
    app.teardown_appcontext(close_db)

    # adds a new command that can be called with the flask command.
    app.cli.add_command(init_db_command)
    


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()