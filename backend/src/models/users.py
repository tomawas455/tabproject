from .db import db, BaseModel


class Role(BaseModel):
    __tablename__ = 'roles'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.Unicode(100))

    _default_fields = ['name']

    def __init__(self, name):
        self.name = name


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(200), nullable=False, unique=True)
    name = db.Column(db.Unicode(100), nullable=False)
    surname = db.Column(db.Unicode(100), nullable=False)
    password = db.Column(db.UnicodeText(), nullable=False)
    role_id = db.Column(
        db.SmallInteger, db.ForeignKey(Role.id), nullable=False)

    role = db.relationship(Role)

    _default_fields = ['email', 'name', 'surname', 'role']
    _hidden_fields = ['password']

    def __init__(self, email, name, surname, password, role):
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.role = role
