from flask import (
    Blueprint, request, session
)

from werkzeug.exceptions import (
    BadRequest, NotFound
)

from access_guards import only_worker

from models.db import db
from models.courses import Course
from models.users import User
from models.courses_utils import Multimedia, Tag
from models.trainings import Training

bp = Blueprint('courses', __name__, url_prefix='/courses')


def check_string(s):
    if type(s)!=str or len(s) == 0:
        return False
    return True


def check_number(n):
    try:
        float(n)
    except (ValueError, TypeError):
        return False
    return True


def check_list(l):
    if type(l)!=list or len(l) == 0:
        return False
    return True


@bp.route('/create', methods=['POST'])
@only_worker
def create_course():
    data_json = request.get_json()
    if not data_json:
        raise BadRequest()
    required_fields = ("name", "description", "expense")
    if(any(field not in data_json for field in required_fields)):
        raise BadRequest(f"Missing required fields: "
            f"{''.join([field + ', ' for field in required_fields if field not in data_json])[:-2]}")
    current_user_id = session["session_id"]
    current_user = User.query.filter_by(id=current_user_id).first()
    if not check_string(data_json["name"]):
        raise BadRequest('"name" should be a non-empty string!')
    if not check_string(data_json["description"]):
        raise BadRequest('"description" should be a non-empty string!')
    if not check_number(data_json["expense"]):
        raise BadRequest('"expense" should be a number!')
    new_course = Course(data_json["name"], data_json["description"],
                    data_json["expense"], current_user)
    if "tags" in data_json:
        if not check_list(data_json["tags"]):
            raise BadRequest('"tags" should be a non-empty list!')
        tags = db.session.query(Tag).filter(Tag.id.in_(data_json["tags"]))
        new_course.tags.extend(tags)
    if "multimedias" in data_json:
        if not check_list(data_json["multimedias"]):
            raise BadRequest('"multimedias" should be a non-empty list!')
        multimedias = db.session.query(Multimedia).filter(Multimedia.id.in_(data_json["multimedias"]))
        new_course.multimedias.extend(multimedias)
    db.session.add(new_course)
    db.session.commit()
    return new_course.to_dict()


@bp.route('/<int:course_id>', methods=['GET'])
@only_worker
def get_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if(course is None):
        raise NotFound("Course with that id does not exist!")
    return course.to_dict()


@bp.route('/', methods=['GET'])
@only_worker
def get_courses():
    courses_page = Course.query.\
        order_by(Course.id).\
        paginate(error_out=False, max_per_page=9999)
    return {
        "courses": [course.to_dict() for course in courses_page.items],
        "pages": courses_page.pages,
        "page": courses_page.page,
        "page_size": courses_page.per_page,
        "is_last": not courses_page.has_next
    }


def has_someone_enrolled(course : Course):
    trainings = db.session.query(Training).filter_by(course_id=course.id)
    for training in trainings:
        if training.free_places_amount < training.places_amount:
            return True
    return False


@bp.route('/<int:course_id>/edit', methods=['PATCH'])
@only_worker
def edit_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        raise NotFound("Course with that id does not exist!")
    if has_someone_enrolled(course):
        raise BadRequest("Someone has already enrolled on that course!")
    data_json = request.get_json()
    if "name" in data_json:
        if not check_string(data_json["name"]):
            raise BadRequest('"name" should be a non-empty string!')
        course.name = data_json["name"]
    if "description" in data_json:
        if not check_string(data_json["description"]):
            raise BadRequest('"description" should be a non-empty string!')
        course.description = data_json["description"]
    if "expense" in data_json:
        if not check_number(data_json["expense"]):
            raise BadRequest('"expense" should be a number!')
        course.expense = data_json["expense"]
    if "add_tags" in data_json:
        if not check_list(data_json["add_tags"]):
            raise BadRequest('"add_tags" should be a non-empty list!')
        tags_to_add = db.session.query(Tag).filter(Tag.id.in_(data_json["add_tags"]))
        course.tags.extend(tags_to_add)
    if "delete_tags" in data_json:
        if not check_list(data_json["delete_tags"]):
            raise BadRequest('"delete_tags" should be a non-empty list!')
        tags_to_delete = db.session.query(Tag).filter(Tag.id.in_(data_json["delete_tags"]))
        for tag in tags_to_delete:
            if tag in course.tags:
                course.tags.remove(tag)
            else:
                raise BadRequest(f'Course has no tag "{tag.name} (id: {tag.id})" ')
    db.session.commit()
    return course.to_dict()
