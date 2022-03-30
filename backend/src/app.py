from flask import Flask, json
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from models.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql://postgres:postgres@db:5432/tabproject"
)
app.config['SECRET_KEY'] = '04105b8b7bcfa615a1d8e1065f08ef1560e0fa10033c6daf84c44174fa5f07e1f8a641e0b9887f48f0f8faeea21f1f817ee8b9d26def88854eeed8bb9050c7ca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


def create_app():
    from routes import (
        auth
    )
    app.register_blueprint(auth.bp)


create_app()

if __name__ == "__main__":
    app.run(debug=True)
