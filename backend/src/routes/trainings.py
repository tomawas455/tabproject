from flask import Blueprint, request, g
from werkzeug.exceptions import NotFound, MethodNotAllowed, BadRequest

from access_guards import only_worker
from utils import datetime_from_json

from models.db import db
from models.trainings import Training
from models.courses import Course
from models.users import User, Role
from models.courses_utils import Tag, Place

bp = Blueprint('trainings', __name__, url_prefix='/trainings')


@bp.route('/<int:id>')
def get_training(id):
    training = Training.query.filter_by(id=id).first()
    if training is None:
        raise NotFound('Training with that id does not exist!')
    return training.to_dict()


@bp.route('/')
def get_trainings():
    json_body = request.get_json()
    trainings_pages = Training.query
    page = 1
    per_page = 20

    if json_body is not None:
        tags = json_body.get('tags')
        if tags:
            trainings_pages = trainings_pages.join(Training.course).join(
                Course.tags).filter(Tag.id.in_(tags))

        name = json_body.get('name')
        if name:
            trainings_pages = trainings_pages.join(
                Training.course).filter(Course.name.ilike('%{}%'.format(name)))

        cities = json_body.get('cities')
        if cities:
            trainings_pages = trainings_pages.join(
                Training.place).filter(Place.city_id.in_(cities))

        page = json_body.get('page', 1)
        per_page = json_body.get('per_page', 20)

    trainings_pages = trainings_pages.order_by(Training.id).paginate(
        page, per_page,
        error_out=False, max_per_page=9999)

    return {
        'trainings': [
            training.to_dict()
            for training in trainings_pages.items
        ],
        'items': len(trainings_pages.items),
        'pages': trainings_pages.pages,
        'page': trainings_pages.page,
        'page_size': trainings_pages.per_page,
        'is_last': not trainings_pages.has_next
    }


def get_instructor(instructor_id):
    instructor = User.query.filter_by(id=instructor_id).join(
        User.role).filter(Role.name == "worker").first()
    if instructor is None:
        raise BadRequest(
            "User with that id does not exist or is not a worker!")
    return instructor


@bp.route('/', methods=['POST'])
@only_worker
def create_training():
    request_body = request.form
    attrs = [
        request_body.get('price'), request_body.get('places_amount'),
        request_body.get('begin_date'), request_body.get('end_date'),
        request_body.get('enrolment_begin_date'), request_body.get(
            'enrolment_end_date'),
        request_body.get('course_id'), request_body.get('place_id'),
        request_body.get('instructor_id')
    ]
    if None in attrs:
        raise BadRequest("Give me all necessary data to create training!")
    course = Course.query.filter_by(id=attrs[6]).first()
    place = Place.query.filter_by(id=attrs[7]).first()
    instructor = get_instructor(attrs[8])
    if None in [course, place]:
        raise BadRequest("course or place with given id does not exist!")
    training = Training(
        attrs[0], attrs[1], attrs[1],
        datetime_from_json(attrs[2]), datetime_from_json(attrs[3]),
        datetime_from_json(attrs[4]), datetime_from_json(attrs[5]),
        course, place, g.user, instructor
    )
    db.session.add(training)
    db.session.commit()
    return training.to_dict()


@bp.route('/<int:id>', methods=['PATCH'])
@only_worker
def edit_training(id):
    request_body = request.form
    training = Training.query.filter_by(id=id).first()
    if training is None:
        raise NotFound("Training with that id does not exist")

    if len(training.participants) > 0:
        raise MethodNotAllowed(
            'Course Cannot have any participants to edit it!')

    price = request_body.get('price')
    if price is not None:
        training.price = float(price)

    places_amount = request_body.get('places_amount')
    if places_amount is not None:
        training.places_amount = int(places_amount)
        training.free_places_amount = int(places_amount)

    begin_date = request_body.get('begin_date')
    if begin_date is not None:
        training.begin_date = datetime_from_json(begin_date)

    end_date = request_body.get('end_date')
    if end_date is not None:
        training.end_date = datetime_from_json(end_date)

    enrolment_begin_date = request_body.get('enrolment_begin_date')
    if enrolment_begin_date is not None:
        training.enrolment_begin_date = datetime_from_json(
            enrolment_begin_date)

    enrolment_end_date = request_body.get('enrolment_end_date')
    if enrolment_end_date is not None:
        training.enrolment_end_date = datetime_from_json(enrolment_end_date)

    place_id = request_body.get('place_id')
    if place_id is not None:
        place = Place.query.filter_by(id=place_id).first()
        if place is None:
            raise BadRequest("Place with that id does not exist!")
        training.place = place

    instructor_id = request_body.get('instructor_id')
    if instructor_id is not None:
        instructor = get_instructor(instructor_id)
        training.instructor = instructor

    db.session.commit()
    return training.to_dict()
