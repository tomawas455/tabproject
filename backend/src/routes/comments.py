import datetime

from flask import Blueprint, request, g
from models.comments import Comment
from models.courses import Course
from werkzeug.exceptions import BadRequest
from models.db import db
from datetime import datetime
from access_guards import only_user

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('/', methods=['POST'])
@only_user
def create_comment():
    request_body = request.form
    text = request_body.get('text')
    creation_time = datetime.now()
    rate = request_body.get('rate')
    author_id = g.user.id
    course_id = request_body.get('course_id')

    if not text or not rate or not course_id:
        raise BadRequest('All parameters should be not an empty string!')

    if Course.query.filter_by(id=course_id).count() == 0:
        raise BadRequest('Course with this id does not exist!')

    if rate > 5 or rate < 0:
        raise BadRequest('Rate must be between 0 and 5!')

    comment = Comment(text, creation_time, rate, author_id, course_id)
    db.session.add(comment)
    db.session.commit()

    return comment.to_dict()