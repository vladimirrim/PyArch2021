from flask import Blueprint, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from api import db
from api.book.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login_post():
    data = request.get_json()
    email = data['email']
    password = data['password']
    remember = data['remember']

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": 'Wrong username or password'}), 400

    login_user(user, remember=remember)
    return jsonify({"result": 'OK'}), 200


@auth.route('/signup', methods=['POST'])
def signup_post():
    data = request.get_json()
    email = data['email']
    name = data['name']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"error": 'Email address already exists'}), 400

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"result": 'OK'}), 200


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"result": 'OK'}), 200