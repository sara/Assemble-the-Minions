#!venv/bin/python
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_pyfile('../config.py')

CHIEF_YOUTH_INSPIRER = "+17327591778"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from views import *
