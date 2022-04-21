from flask import Blueprint, request, json
from models.courses_utils import City
from werkzeug.exceptions import BadRequest
from models.db import db

bp = Blueprint('cities', __name__, url_prefix='/cities')

@bp.route('/', methods=['GET'])
def get_cities():
    cities = City.query.order_by(City.id)
    return json.jsonify([city.to_dict() for city in cities])

@bp.route('/', methods=['POST'])
def create_city():
    name = request.form.get('city')
    cities = City.query
    if name == "":
        raise BadRequest('Parameter should not be an empty string')
    for city in cities:
        if city.city == name:
            raise BadRequest('This City arleady exist!')
    city = City(name)
    db.session.add(city)
    db.session.commit()
    return city.to_dict()