from .db import db, BaseModel
from .users import User

course_tags_M2M = db.Table(
    'course_tags', BaseModel.metadata,
    db.Column('course_id', db.Integer, db.ForeignKey(
        'courses.id'), primary_key=True),
    db.Column('tag_id', db.SmallInteger,
              db.ForeignKey('tags.id'), primary_key=True)
)


class Course(BaseModel):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    description = db.Column(db.UnicodeText(), nullable=False)
    expense = db.Column(db.Numeric(50, 2), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    author = db.relationship(User, lazy='subquery')
    multimedias = db.relationship('Multimedia')
    tags = db.relationship('Tag', secondary=course_tags_M2M, lazy='subquery')

    _default_fields = ['id', 'name', 'description',
                       'author', 'multimedias', 'tags', 'expense']

    def __init__(self, name, description, expense, author):
        self.name = name
        self.description = description
        self.expense = expense
        self.author = author
