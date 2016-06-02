#!flask/bin/python
from app.models.db import db
from app.models.user import *
from app.models.profile import *
db.create_all()


