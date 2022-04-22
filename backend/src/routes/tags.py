from flask import Blueprint, request, json
from models.courses_utils import Tag
from werkzeug.exceptions import BadRequest
from models.db import db

from access_guards import only_worker

bp = Blueprint('tags', __name__, url_prefix='/tags')


@bp.route('/', methods=['GET'])
def get_tags():
    tags = Tag.query.order_by(Tag.id)
    return json.jsonify([tag.to_dict() for tag in tags])


@bp.route('/', methods=['POST'])
@only_worker
def create_tag():
    name = request.form.get('name')

    if not name:
        raise BadRequest('Parameter should not be an empty string')

    if Tag.query.filter(Tag.name.ilike(name)).count() > 0:
        raise BadRequest('This Tag arleady exist!')

    tag = Tag(name)
    db.session.add(tag)
    db.session.commit()
    return tag.to_dict()
