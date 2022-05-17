from flask import (
    Blueprint, request, session
)
from werkzeug.security import check_password_hash
from werkzeug.exceptions import Unauthorized

from models.db import db
from models.users import User
from register_user import register_user

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    name = request.form['name']
    surname = request.form['surname']
    password = request.form['password']
    new_user = register_user(email, name, surname, password)
    db.session.commit()
    return new_user.to_dict()


@bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email.lower()).first()
    if user is None or not check_password_hash(user.password, password):
        raise Unauthorized("Wrong login and/or password")
    session.clear()
    session['session_id'] = user.id
    return user.to_dict()


@bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return {}
