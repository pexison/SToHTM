from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Flask application and database registration
app = Flask(__name__, static_url_path='')
db = SQLAlchemy(app)

# Route and config registration
from app.routes import index
from app.api.user_api import user

app.config.from_object('config')
app.register_blueprint(user)
