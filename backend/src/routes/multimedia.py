from flask import Blueprint, request
from models.courses_utils import Multimedia
from models.courses import Course
from models.db import db

from werkzeug.exceptions import BadRequest, NotFound

from access_guards import only_worker

bp = Blueprint('multimedia', __name__, url_prefix='/multimedia')


@bp.route('/<int:course_id>', methods=['POST'])
@only_worker
def edit_multimedia(course_id):
    request_body = request.form
    filename = request_body.get('filename')

    if not filename:
        raise BadRequest('Filename should be not an empty string!')

    if Course.query.filter_by(id=course_id).count() == 0:
        raise BadRequest('Course with this id does not exist!')

    multimedia = Multimedia(filename, course_id)
    db.session.add(multimedia)
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
