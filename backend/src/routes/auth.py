from flask import (
    Blueprint, request, g, session
)
from werkzeug.security import (
    check_password_hash, generate_password_hash
)
from werkzeug.exceptions import (
    BadRequest, InternalServerError, Unauthorized
)

from models.db import db
from models.users import Role, User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    name = request.form['name']
    surname = request.form['surname']
    password = request.form['password']
    if len(name) < 1 or len(surname) < 1:
        raise BadRequest(
            "Name and surname need to have at least one character")
    if len(password) < 8:
        raise BadRequest("Password need to have at least 8 characters")
    email_taken = User.query.filter_by(email=email.lower()).count()
    user_role = Role.query.filter_by(name='user').first()
    if user_role is None:
        raise InternalServerError(
            "Cannot create user, report this error please")
    if email_taken > 0:
        raise BadRequest("That email is already in use")
    password = generate_password_hash(password)
    new_user = User(email.lower(), name, surname, password, user_role)
    db.session.add(new_user)
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
