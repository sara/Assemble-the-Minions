#!venv/bin/python
from minions import db
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    file = db.Column(db.String(128), default=None)
    email = db.Column(db.String(64), default=None)
    xd_id = db.Column(db.Integer, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

class Ambassador(db.Model):
    __tablename__ = 'ambassadors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Integer)
    ethnicity = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    year = db.Column(db.String(64))

class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    weekday = db.Column(db.String(64))
    start = db.Column(db.Float)
    end = db.Column(db.Float)
    ambassador_id = db.Column(db.Integer, db.ForeignKey('ambassadors.id'), nullable=False)
