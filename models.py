from sqlalchemy.ext.hybrid import hybrid_method

from create_db import db
from password_protection import check_encrypted_password


class User(db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    accessPrivilege = db.Column(db.Integer, nullable=False)
    patentInfo = db.relationship('Patent', backref='user', lazy=True)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


class Patent(db.Model):
    __bind_key__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(120), unique=True, nullable=False)
    accountBalance = db.Column(db.String(120), unique=True, nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    visits = db.relationship('Visit', backref='patent', lazy=True)

    def __repr__(self):
        return '<Patent %r>' % self.name


class Visit(db.Model):
    __bind_key__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Integer,)
    patent_id = db.Column(db.Integer, db.ForeignKey('patent.id'),
        nullable=False)

    def __repr__(self):
        return '<Visit %r>' % self.name