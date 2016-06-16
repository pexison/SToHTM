#!flask/bin/python
from app.models.db import db
from app.models.user import *
from app.models.profile import *
from app.models.category import *
from app.models.service import *
db.create_all()
