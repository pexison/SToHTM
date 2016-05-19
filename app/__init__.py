from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='')
app.config.from_object('config')
from app.routes import index
from app.api.user_api import user
db = SQLAlchemy(app)
app.register_blueprint(user)
