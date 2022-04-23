from flask import Blueprint, request, json
from models.trainings import Meeting, Training
from werkzeug.exceptions import BadRequest
from models.db import db

from access_guards import only_worker

bp = Blueprint('meetings', __name__, url_prefix='/meetings')


@bp.route('/', methods=['POST'])
def create_meeting():
    request_body = request.form
    begin_date = request_body.get('begin_date')
    end_date = request_body.get('end_date')
    training_id = request_body.get('training_id')

    if not begin_date or not end_date or not training_id:
        raise BadRequest('All parameters should be not an empty string!')

    if Training.query.filter_by(id=training_id).count() == 0:
        raise BadRequest('Training with this id does not exist!')

    meeting = Meeting(begin_date, end_date, training_id)

    db.session.add(meeting)
    db.session.commit()

    return meeting.to_dict()