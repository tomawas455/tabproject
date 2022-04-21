from flask import Blueprint, request, json
from models.courses_utils import Place, City
from werkzeug.exceptions import BadRequest
from models.db import db

from access_guards import only_worker

bp = Blueprint('places', __name__, url_prefix='/places')

@bp.route('/', methods=['GET'])
def get_places():
    places = Place.query.order_by(Place.id)
    return json.jsonify([place.to_dict() for place in places])

@bp.route('/', methods=['POST'])
@only_worker
def create_place():
    request_body = request.form
    attrs = [
        request_body.get('address'),
        request_body.get('city_id')
    ]
    if None in attrs:
        raise BadRequest("All parameters should be not an empty string!")
    city = City.query.filter_by(id=attrs[1]).first()
    if not city:
        raise BadRequest("City with this id doesn't exist!")
    places = Place.query
    for place in places:
        if place.address == attrs[0] and place.city_id == city.id:
                    raise BadRequest("This place already exist!")

    place = Place(attrs[0], city)
    db.session.add(place)
    db.session.commit()
    return place.to_dict()