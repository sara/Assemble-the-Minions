#!venv/bin/python
from minions import db
from flask.ext.login import UserMixin

class Ambassador(db.Model):
    __tablename__ = 'ambassadors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    phone = db.Column(db.String)
    ethnicity = db.Column(db.String(45))
    gender = db.Column(db.String(45))
    numvisits = db.Column(db.String(45))
    rank = db.Column(db.String(45))
    gradcode = db.Column(db.String(45))

class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(45))
    start = db.Column(db.Float)
    end = db.Column(db.Float)
