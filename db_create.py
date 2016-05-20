#!flask/bin/python
from app.models.db import db
from app.models.user import *
db.create_all()


