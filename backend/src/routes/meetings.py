from flask import Blueprint, request, json
from models.trainings import Meeting, Training
from werkzeug.exceptions import BadRequest, NotFound
from models.db import db

from access_guards import only_worker

bp = Blueprint('meetings', __name__, url_prefix='/meetings')


@bp.route('/', methods=['POST'])
@only_worker
def create_meeting():
    request_body = request.form
    begin_date = request_body.get('begin_date')
    end_date = request_body.get('end_date')
    training_id = request_body.get('training_id')

    if not begin_date or not end_date or not training_id:
        raise BadRequest('All parameters should be not an empty string!')

    if Training.query.filter_by(id=training_id).count() == 0:
        raise BadRequest('Training with this id does not exist!')

    if begin_date > end_date:
        raise BadRequest('Begin date have to be before end date!')

    meeting = Meeting(begin_date, end_date, training_id)

    db.session.add(meeting)
    db.session.commit()

    return meeting.to_dict()


@bp.route('/<int:meeting_id>', methods=['PATCH'])
@only_worker
def edit_meeting(meeting_id):
    request_body = request.form
    meeting = Meeting.query.filter_by(id=meeting_id).first()
    begin_date = request_body.get('begin_date')
    end_date = request_body.get('end_date')
    training_id = request_body.get('training_id')

    if not meeting:
        raise NotFound('Meeting with this id does not exsist!')

    if not begin_date or not end_date or not training_id:
        raise BadRequest('All parameters should be not an empty string!')

    if Training.query.filter_by(id=training_id).count() == 0:
        raise BadRequest('Training with this id does not exist!')

    if begin_date > end_date:
        raise BadRequest('Begin date have to be before end date!')

    meeting.begin_date = begin_date
    meeting.end_date = end_date
    meeting.training_id = training_id

    db.session.commit()

    return meeting.to_dict()
