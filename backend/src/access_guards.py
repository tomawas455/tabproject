import functools

from flask import g
from werkzeug.exceptions import Unauthorized


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            raise Unauthorized("You need to login to see this")

        return view(**kwargs)

    return wrapped_view


def check_role(role_name):
    if g.user is None or g.user.role.name != role_name:
        raise Unauthorized(
            "You need to have different permissions to see this"
        )


def only_worker(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        check_role('worker')
        return view(**kwargs)

    return wrapped_view


def only_admin(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        check_role('administrator')
        return view(**kwargs)

    return wrapped_view
