from operator import and_, or_
from flask import Blueprint, request, json, g
from models.trainings import Participation, Training
from werkzeug.exceptions import BadRequest
from models.db import db

from access_guards import only_worker, only_user

bp = Blueprint('raports', __name__, url_prefix='/raports')


@only_worker
@bp.route('/worker', methods=['GET'])
def get_worker_raport():
    data_json = request.get_json()
    filters = []
    if "from_date" in data_json:
        filters.append((Training.begin_date >= data_json["from_date"]))
    if "to_date" in data_json:
        filters.append((Training.begin_date <= data_json["to_date"]))
    if "courses" in data_json and data_json["courses"]:
        filters.append((Training.course_id.in_(data_json["courses"])))
    if "trainings" in data_json and data_json["trainings"]:
        filters.append((Training.course_id.in_(data_json["trainings"])))
    if "authors" in data_json and data_json["authors"]:
        filters.append((Training.author_id.in_(data_json["authors"])))
    if "instructors" in data_json and data_json["instructors"]:
        filters.append((Training.instructor_id.in_(data_json["instructors"])))
    trainings_page = db.session.query(Training) \
                                .filter(*filters) \
                                .paginate(error_out=False, max_per_page=9999)
    res = []
    for training in trainings_page.items:
        income = (len(training.participants)*training.price) - training.course.expense
        res.append(training.to_dict())
        res[-1]["income"] = income

    return {
        "trainings": res,
        "items": len(res),
        "pages": trainings_page.pages,
        "page": trainings_page.page,
        "page_size": trainings_page.per_page,
        "is_last": not trainings_page.has_next
    }


@bp.route('/user', methods=['GET'])
@only_user
def get_user_raport():
    data_json = request.get_json()
    participations = Participation.query.filter(or_(Participation.user_id==g.user.id,
                                                    Participation.payer_id==g.user.id)).all()
    filters = []
    filters.append((Training.id.in_([participation.training_id for participation in participations])))
    if "from_date" in data_json:
        filters.append((Training.begin_date >= data_json["from_date"]))
    if "to_date" in data_json:
        filters.append((Training.begin_date <= data_json["to_date"]))
    if "courses" in data_json and data_json["courses"]:
        filters.append((Training.course_id.in_(data_json["courses"])))
    trainings_page = db.session.query(Training) \
                            .filter(*filters) \
                            .paginate(error_out=False, max_per_page=9999)
    res = []
    already_counted_trainings = []
    for training in trainings_page.items:
        if training.id not in already_counted_trainings:
            res.append(training.to_dict())
            user_expense = training.price * sum(1 for participation in participations 
                                                if participation.payer_id == g.user.id 
                                                and participation.training_id == training.id)
            res[-1]["user_expense"] = user_expense
            already_counted_trainings.append(training.id)

    return {
        "trainings": res,
        "items": len(res),
        "pages": trainings_page.pages,
        "page": trainings_page.page,
        "page_size": trainings_page.per_page,
        "is_last": not trainings_page.has_next
    }
