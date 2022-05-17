from werkzeug.security import generate_password_hash
from werkzeug.exceptions import (
    BadRequest, InternalServerError
)

from models.db import db
from models.users import Role, User


# it does not commit user to db as someone may want to register multiple users
# and it would be embarassing to have some users end up registered
# and some not
def register_user(email, name, surname, password):
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
    return new_user
