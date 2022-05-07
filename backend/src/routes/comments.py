import datetime

from flask import Blueprint, request, g
from models.comments import Comment
from models.courses import Course
from models.trainings import Participation, Training
from werkzeug.exceptions import BadRequest
from models.db import db
from datetime import datetime
from access_guards import only_user

bp = Blueprint('comments', __name__, url_prefix='/comments')


def is_trainee(user_id, course_id):
    parts = Participation.query.filter_by(user_id=user_id)
    if not parts:
        return False
    trainings = Training.query.filter_by(course_id=course_id)
    for p in parts:
        for t in trainings:
            if p.training_id == t.id:
                return True
    return False


@bp.route('/<int:course_id>', methods=['POST'])
@only_user
def create_comment(course_id):
    request_body = request.form
    text = request_body.get('text')
    creation_time = datetime.now()
    rate = request_body.get('rate')
    author = g.user

    if not rate:
        raise BadRequest('You need to rate the course!')

    try:
        rate = int(rate)
    except:
        raise BadRequest('Rate must be integer!')

    if not text:
        raise BadRequest('You can not send empty comment!')

    if rate > 5 or rate < 0:
        raise BadRequest('Rate must be between 0 and 5!')

    if Course.query.filter_by(id=course_id).count() == 0:
        raise BadRequest('Course with this id does not exist!')

    if not is_trainee(user_id=author.id, course_id=course_id):
        raise BadRequest('To comment on the course you must first take part in it!')

    comment = Comment(text, creation_time, rate, author, Course.query.filter_by(id=course_id).first())

    db.session.add(comment)
    db.session.commit()

    return comment.to_dict()
