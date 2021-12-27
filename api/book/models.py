from flask_login import UserMixin

from api import db


class User(UserMixin, db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Book(db.Model):
    __bind_key__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    library_id = db.Column(db.Integer)
    title = db.Column(db.String)
    author = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "author": self.author,
                "description": self.description,
                "created_at": str(self.created_at.strftime('%d-%m-%Y'))}
