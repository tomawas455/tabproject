from .db import db, BaseModel


class Comment(BaseModel):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(256), nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False)
    rate = db.Column(db.SmallInteger, nullable=False)

    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User')

    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    course = db.relationship('Course')

    _default_fields = ['id', 'text', 'creation_time',
                       'rate', 'author', 'course_id']

    def __init__(self, text, creation_time, rate, author, course):
        self.text = text
        self.creation_time = creation_time
        self.rate = rate
        self.author = author
        self.course = course
