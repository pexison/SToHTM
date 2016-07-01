from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Flask application and database registration
app = Flask(__name__, static_url_path='')
db = SQLAlchemy(app)

# Route and config registration
from app.routes import index
from app.api.user_api import user
from app.api.session_api import auth
from app.api.profile_api import profile
from app.api.categories_api import category
from app.api.services_api import service
from app.api.quotation_api import quotation

app.config.from_object('config')
app.register_blueprint(user)
app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(category)
app.register_blueprint(service)
app.register_blueprint(quotation)
