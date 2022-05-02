from flask import Blueprint, request, json
from models.courses_utils import Multimedia
from models.courses import Course
from models.db import db

from werkzeug.exceptions import BadRequest, NotFound

from access_guards import only_worker

bp = Blueprint('multimedia', __name__, url_prefix='/multimedia')


@bp.route('/<int:multimedia_id>', methods=['PATCH'])
@only_worker
def edit_multimedia(multimedia_id):
    request_body = request.form
    multimedia = Multimedia.query.filter_by(id=multimedia_id).first()
    course_id = request_body.get('course_id')
    filename = request_body.get('filename')

    if not multimedia:
        raise NotFound('Multimedia with this id does not exist!')

    if not course_id or not filename:
        raise BadRequest('All parameters should be not an empty string!')

    if Course.query.filter_by(id=course_id).count() == 0:
        raise BadRequest('Course with this id does not exist!')

    multimedia.filename = filename
    multimedia.course_id = int(course_id)

    db.session.commit()
    return multimedia.to_dict()


@bp.route('/<int:multimedia_id>', methods=['DELETE'])
@only_worker
def delete_multimedia(multimedia_id):
    multimedia = Multimedia.query.filter_by(id=multimedia_id).first()

    if not multimedia:
        raise NotFound('Multimedia with this id does not exist!')

    db.session.delete(multimedia)
    db.session.commit()

    return multimedia.to_dict()
