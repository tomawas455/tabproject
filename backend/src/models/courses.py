from .db import db, BaseModel
from .users import User


class Course(BaseModel):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    description = db.Column(db.UnicodeText(), nullable=False)
    expense = db.Column(db.Numeric(50, 2), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __init__(self, name, description, expense, author):
        self.name = name
        self.description = description
        self.expense = expense
        self.author = author
