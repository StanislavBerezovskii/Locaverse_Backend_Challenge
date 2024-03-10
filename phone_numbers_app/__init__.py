import os
from flask import Flask

from .api_views import main
from .error_handlers import errors
from .extensions import db
from .models import PhoneNumber


def create_app(database_uri=os.getenv('DATABASE_URI')):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', default='qwerty12345')
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app
