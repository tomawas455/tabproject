from flask import (
    Blueprint, request, session, g
)

from werkzeug.exceptions import (
    BadRequest, NotFound
)

from access_guards import only_worker
from models.courses import Course

from models.db import db
from models.trainings import Participation, Training

bp = Blueprint('participations', __name__, url_prefix='/participations')


@bp.route('/', methods=['GET'])
@only_worker
def get_participants():
    training_id = request.form.get("training_id")
    training = Training.query.filter_by(id=training_id).first()
    if(training is None):
        raise NotFound("Training with that id does not exist!")
    participations_page = (Participation.query.filter_by(training_id=training_id)
                    .paginate(error_out=False, max_per_page=9999))
    return {
        "participants": [participant.to_dict() for participant in participations_page.items],
        "pages": participations_page.pages,
        "page": participations_page.page,
        "page_size": participations_page.per_page,
        "is_last": not participations_page.has_next
    }