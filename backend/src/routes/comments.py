import datetime

from flask import Blueprint, request, g, json
from models.comments import Comment
from models.courses import Course
from models.trainings import Participation, Training
from werkzeug.exceptions import BadRequest, NotFound
from models.db import db
from datetime import datetime
from access_guards import only_user_or_worker

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('/<int:course_id>', methods=['POST'])
@only_user_or_worker
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
    except ValueError:
        raise BadRequest('Rate must be integer!')

    if not text:
        raise BadRequest('You can not send empty comment!')

    if rate > 5 or rate < 0:
        raise BadRequest('Rate must be between 0 and 5!')

    course = Course.query.filter_by(id=course_id).first()

    if course is None:
        raise BadRequest('Course with this id does not exist!')

    if db.session.query(Participation)\
        .join(Training, Participation.training_id == Training.id)\
        .filter(Participation.user_id == g.user.id, Training.course_id == course_id).count() == 0:

        raise BadRequest('To comment on the course you must first take part in it!')

    comment = Comment(text, creation_time, rate, author, course)

    db.session.add(comment)
    db.session.commit()

    return comment.to_dict()
