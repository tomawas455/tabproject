import functools

from flask import g
from werkzeug.exceptions import Unauthorized
import sys


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            raise Unauthorized("You need to login to see this")

        return view(**kwargs)

    return wrapped_view


def check_roles(role_names):
    print(g.user.role.name, file=sys.stderr)
    if g.user is None or g.user.role.name not in role_names:
        raise Unauthorized(
            "You need to have different permissions to see this"
        )


def only_user(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        check_roles(['user'])
        return view(**kwargs)

    return wrapped_view


def only_worker(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        check_roles(['worker'])
        return view(**kwargs)

    return wrapped_view


def only_admin(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        check_roles(['administrator'])
        return view(**kwargs)

    return wrapped_view


def only_user_or_worker(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        check_roles(['user', 'worker'])
        return view(**kwargs)

    return wrapped_view
