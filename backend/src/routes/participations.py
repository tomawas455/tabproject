from operator import and_
from flask import (
    Blueprint, request, session, g
)

from werkzeug.exceptions import (
    BadRequest, NotFound
)

from datetime import datetime

from access_guards import only_user, only_worker
from register_user import register_user

from models.db import db
from models.trainings import Participation, Training

bp = Blueprint('participations', __name__, url_prefix='/participations')


@bp.route('/', methods=['GET'])
@only_worker
def get_participants():
    training_id = request.form.get("training_id")
    training = Training.query.filter_by(id=training_id).first()
    if training is None:
        raise NotFound("Training with that id does not exist!")
    participations_page = (Participation.query.filter_by(training_id=training_id)
                    .paginate(error_out=False, max_per_page=9999))
    return {
        "participants": [participant.to_dict() for participant in participations_page.items],
        "pages": participations_page.pages,
        "page": participations_page.page,
        "page_size": participations_page.per_page,
        "is_last": not participations_page.has_next
    }


@bp.route('/', methods=['POST'])
@only_user
def create_participants():
    data_json = request.get_json()
    if "training_id" not in data_json or type(data_json["training_id"]) is not int:
        raise BadRequest("Required parameter: 'training_id'")
    training_id = data_json["training_id"]
    training = Training.query.filter_by(id=training_id).first()
    if not training:
        raise NotFound("Training with this id does not exist!")
    if training.enrolment_begin_date > datetime.today():
        raise BadRequest("You can not enroll on this training yet!")
    if training.enrolment_end_date < datetime.today():
        raise BadRequest("You can not enroll on this training anymore!")
    if "users_to_register" not in data_json or type(data_json["users_to_register"]) is not list:
        raise BadRequest("Required parameter: 'users_to_register' list of emails and passwords")
    if training.free_places_amount < len(data_json["users_to_register"]) + 1:
        raise BadRequest(f"There are not enough free places! Free places: {training.free_places_amount}")
    already_enrolled = Participation.query.filter(and_(Participation.training_id==training_id,
                                                    Participation.user_id==g.user.id)).first()
    if already_enrolled:
        raise BadRequest(f"User has already enrolled")
    users_to_enroll = [g.user]
    for user in data_json["users_to_register"]:
        added_user = register_user(user["email"], user["name"], user["surname"], user["password"])
        users_to_enroll.append(added_user)
    db.session.commit()
    participants = [Participation(training_id=training_id, user_id=user.id) for user in users_to_enroll]
    db.session.add_all(participants)
    training.free_places_amount -= len(participants)
    db.session.commit()
    return {"participants":[participant.to_dict() for participant in participants]}


@bp.route('/', methods=['PATCH'])
@only_worker
def edit_participation():
    data_json = request.get_json()
    if any(parameter not in data_json for parameter in ("user_id", "training_id", "passed")):
        raise BadRequest("Required parameters: user_id, training_id")
    participation = Participation.query.filter_by(user_id=data_json["user_id"], training_id=data_json["training_id"]).first()
    if participation is None:
        raise NotFound("Participation with this user id and training id does not exist!")
    participation.passed = data_json["passed"]
    db.session.commit()
    return participation.to_dict()
