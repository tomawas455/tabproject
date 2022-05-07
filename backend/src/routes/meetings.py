from flask import Blueprint, request, g, json
from models.trainings import Meeting, Training
from werkzeug.exceptions import BadRequest, NotFound
from models.db import db
from src.utils import datetime_from_json
from access_guards import only_worker
from models.trainings import Participation, Training
import datetime

bp = Blueprint('meetings', __name__, url_prefix='/meetings')


def string_to_date(date):
    result = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return result


@bp.route('/', methods=['POST'])
@only_worker
def create_meeting():
    request_body = request.form
    training_id = request_body.get('training_id')
    begin_date = request_body.get('begin_date')
    end_date = request_body.get('end_date')

    if not begin_date or not end_date or not training_id:
        raise BadRequest('All parameters should be not an empty string!')

    if Training.query.filter_by(id=training_id).count() == 0:
        raise BadRequest('Training with this id does not exist!')

    try:
        begin_date = datetime_from_json(begin_date)
        end_date = datetime_from_json(end_date)
    except:
        raise BadRequest('Invalid format of date. Date must be YYYY-MM-DDTHH:MM:SS.00Z')

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

    if not meeting:
        raise NotFound('Meeting with this id does not exsist!')

    if not begin_date and not end_date:
        raise BadRequest('Nothing to edit..')

    try:
        if not begin_date:
            begin_date = meeting.begin_date
        else:
            begin_date = datetime_from_json(begin_date)

        if not end_date:
            end_date = meeting.end_date
        else:
            end_date = datetime_from_json(end_date)
    except:
        raise BadRequest('Invalid format of date. Date must be YYYY-MM-DDTHH:MM:SS.00Z')

    if begin_date > end_date:
        raise BadRequest('Begin date have to be before end date!')

    meeting.begin_date = begin_date
    meeting.end_date = end_date

    db.session.commit()

    return meeting.to_dict()


@bp.route('/<int:meeting_id>', methods=['DELETE'])
@only_worker
def delete_meeting(meeting_id):
    meeting = Meeting.query.filter_by(id=meeting_id).first()

    if not meeting:
        raise NotFound('Meeting with this id does not exsist!')

    if Training.query.filter_by(id=meeting.training_id, instructor_id=g.user.id).count() == 0:
        raise BadRequest('You cannot delete meeting if you are not trainer of this!')

    if Participation.query.filter_by(training_id=meeting.training_id).count() != 0:
        raise BadRequest('You can not delete meeting with trainees!')

    db.session.delete(meeting)
    db.session.commit()

    return meeting.to_dict()
