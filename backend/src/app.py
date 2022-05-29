import traceback

from flask import Flask, json, g, session
from flask_migrate import Migrate
from flask_cors import CORS
from werkzeug.exceptions import HTTPException, InternalServerError

from models.db import db
from models.users import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql://postgres:postgres@db:5432/tabproject"
)
app.config['SECRET_KEY'] = '04105b8b7bcfa615a1d8e1065f08ef1560e0fa10033c6daf84c44174fa5f07e1f8a641e0b9887f48f0f8faeea21f1f817ee8b9d26def88854eeed8bb9050c7ca'
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_exception(e):
    """Print traceback on error and return http error on unhandled errors"""
    traceback.print_exception(type(e), e, e.__traceback__)
    return handle_http_exception(
        InternalServerError("You probably gave me bad data, fix your input!"))


@app.before_request
def load_logged_in_user():
    session_id = session.get('session_id')
    if session_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=session_id).first()


def create_app():
    from routes import (
        auth, users, trainings, courses, tags,
        places, cities, multimedia, meetings, comments
    )
    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(tags.bp)
    app.register_blueprint(places.bp)
    app.register_blueprint(cities.bp)
    app.register_blueprint(trainings.bp)
    app.register_blueprint(courses.bp)
    app.register_blueprint(multimedia.bp)
    app.register_blueprint(meetings.bp)
    app.register_blueprint(comments.bp)


create_app()

if __name__ == "__main__":
    app.run(debug=True)
