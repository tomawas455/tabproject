from .db import db, BaseModel


class Meeting(BaseModel):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    begin_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    training_id = db.Column(db.Integer, db.ForeignKey(
        'trainings.id'), nullable=False)

    _default_fields = ['id', 'begin_date', 'end_date']

    def __init__(self, begin_date, end_date, training_id):
        self.begin_date = begin_date
        self.end_date = end_date
        self.training_id = training_id


class Participation(BaseModel):
    __tablename__ = 'participations'

    training_id = db.Column(db.Integer, db.ForeignKey(
        'trainings.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
    user = db.relationship('User')

    passed = db.Column(db.Boolean)

    _default_fields = ['id', 'user', 'passed']

    def __init__(self, training_id, user_id):
        self.training_id = training_id
        self.user_id = user_id


class Training(BaseModel):
    __tablename__ = 'trainings'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(50, 2), nullable=False)

    places_amount = db.Column(db.SmallInteger, nullable=False)
    free_places_amount = db.Column(db.SmallInteger, nullable=False)

    begin_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    enrolment_begin_date = db.Column(db.DateTime, nullable=False)
    enrolment_end_date = db.Column(db.DateTime, nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    course = db.relationship('Course', lazy='subquery')

    place_id = db.Column(db.Integer, db.ForeignKey(
        'places.id'), nullable=False)
    place = db.relationship('Place', lazy='subquery')

    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', foreign_keys=author_id, lazy='subquery')

    instructor_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    instructor = db.relationship(
        'User', foreign_keys=instructor_id, lazy='subquery')

    meetings = db.relationship(Meeting)
    participants = db.relationship(Participation)

    _default_fields = [
        'id', 'price',
        'places_amount', 'free_places_amount',
        'begin_date', 'end_date',
        'enrolment_begin_date', 'enrolment_end_date',
        'course', 'place',
        'author', 'instructor', 'meetings'
    ]

    def __init__(
        self, price,
        places_amount, free_places_amount,
        begin_date, end_date,
        enrolment_begin_date, enrolment_end_date,
        course, place, author, instructor
    ):
        self.price = price
        self.places_amount = places_amount
        self.free_places_amount = free_places_amount
        self.begin_date = begin_date
        self.end_date = end_date
        self.enrolment_begin_date = enrolment_begin_date
        self.enrolment_end_date = enrolment_end_date
        self.course = course
        self.place = place
        self.author = author
        self.instructor = instructor
