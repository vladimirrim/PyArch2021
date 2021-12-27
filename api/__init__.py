from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from api.google_books.google_books_api import GoogleBooksAPIManager
from api.permission.permission_manager import PermissionManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config["SQLALCHEMY_BINDS"] = {'users': 'sqlite:///users_db.sqlite',
                                      'library': 'sqlite:///library_db.sqlite',
                                      'books': 'sqlite:///books_db.sqlite',
                                      'reviews': 'sqlite:///reviews_db.sqlite',
                                      'book_permissions': 'sqlite:///book_permissions_db.sqlite',
                                      'user_permissions': 'sqlite:///user_permissions_db.sqlite'}
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from api.auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app


app = create_app()
permission_manager = PermissionManager(db)
google_books_api_manager = GoogleBooksAPIManager()
login_manager = LoginManager()
login_manager.init_app(app)
