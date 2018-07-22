"""Database tools and helpers."""


from datetime import datetime

from click import command, echo
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext


db = SQLAlchemy()


class Post(db.Model):
    """A blog post."""
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    slug = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Post %r (%r)>" % (self.title, self.created)


@command("init-db")
@with_appcontext
def init_db_command():
    """Initialize the database."""
    db.create_all()
    echo("Initialized the database.")


def init_app(app):
    """Initialize the Flask app for database usage."""
    db.init_app(app)
    app.cli.add_command(init_db_command)
