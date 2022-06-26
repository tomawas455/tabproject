from operator import and_
from flask import Blueprint, request, json
from models.trainings import Training
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
    if "courses" in data_json:
        filters.append((Training.course_id.in_(data_json["courses"])))
    if "trainings" in data_json:
        filters.append((Training.course_id.in_(data_json["trainings"])))
    if "authors" in data_json:
        filters.append((Training.author_id.in_(data_json["authors"])))
    if "instructors" in data_json:
        filters.append((Training.instructor_id.in_(data_json["instructors"])))
    trainings_page = db.session.query(Training).filter(*filters).paginate(error_out=False, max_per_page=9999)
    return {
        "trainings": [training.to_dict() for training in trainings_page.items],
        "items": len(trainings_page.items),
        "pages": trainings_page.pages,
        "page": trainings_page.page,
        "page_size": trainings_page.per_page,
        "is_last": not trainings_page.has_next
    }


@bp.route('/user', methods=['GET'])
@only_user
def get_user_raport():
    pass
