from .db import db, BaseModel


class City(BaseModel):
    __tablename__ = 'cities'

    id = db.Column(db.SmallInteger, primary_key=True)
    city = db.Column(db.Unicode(100), nullable=False)

    _default_fields = ['id', 'city']

    def __init__(self, city):
        self.city = city


class Place(BaseModel):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Unicode(500), nullable=False)
    city_id = db.Column(
        db.SmallInteger, db.ForeignKey(City.id), nullable=False)

    city = db.relationship(City)

    _default_fields = ['id', 'address', 'city']

    def __init__(self, address, city):
        self.address = address
        self.city = city


class Tag(BaseModel):
    __tablename__ = 'tags'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)

    _default_fields = ['id', 'name']

    def __init__(self, name):
        self.name = name


class Multimedia(BaseModel):
    __tablename__ = 'multimedias'

    id = db.Column(db.SmallInteger, primary_key=True)
    filename = db.Column(db.Unicode(100), nullable=False)
    course_id = db.Column(
        db.Integer, db.ForeignKey('courses.id'), nullable=False)

    _default_fields = ['id', 'filename']

    def __init__(self, filename, course_id):
        self.filename = filename
        self.course_id = course_id
