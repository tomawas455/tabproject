from flask import Blueprint, request, json
from models.courses_utils import City
from werkzeug.exceptions import BadRequest
from models.db import db

from access_guards import only_worker

bp = Blueprint('cities', __name__, url_prefix='/cities')


@bp.route('/', methods=['GET'])
def get_cities():
    cities = City.query.order_by(City.id)
    return json.jsonify([city.to_dict() for city in cities])


@bp.route('/', methods=['POST'])
@only_worker
def create_city():
    name = request.form.get('city')

    if not name:
        raise BadRequest('Parameter should not be an empty string')

    if City.query.filter(City.city.ilike(name)).count() > 0:
        raise BadRequest('This City arleady exist!')

    city = City(name)
    db.session.add(city)
    db.session.commit()
    return city.to_dict()
