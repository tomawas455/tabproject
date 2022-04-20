from flask import (
    Blueprint, request, g
)
from werkzeug.exceptions import NotFound

from access_guards import only_admin, login_required

from models.db import db
from models.users import User, Role

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/current')
@login_required
def get_current_user():
    return g.user.to_dict()


@bp.route('/')
@only_admin
def get_users():
    users_pages = User.query\
        .order_by(User.id)\
        .paginate(error_out=False, max_per_page=9999)
    all_roles = Role.query.order_by(Role.id)
    return {
        'users': [user.to_dict() for user in users_pages.items],
        'pages': users_pages.pages,
        'page': users_pages.page,
        'page_size': users_pages.per_page,
        'is_last': not users_pages.has_next,
        'roles': [role.to_dict() for role in all_roles]
    }


@bp.route('/<int:user_id>/change_role', methods=['PATCH'])
@only_admin
def change_role(user_id):
    user = User.query.filter_by(id=user_id).first()
    role = Role.query.filter_by(id=request.form['role_id']).first()
    if user is None:
        raise NotFound('User with that id does not exist!')
    if role is None:
        raise NotFound('Role with that id does not exist!')
    user.role = role
    user.role_id = role.id
    db.session.commit()
    return user.to_dict()
