from flask import Flask
# from utils import CustomJSONEncoder
# app.config.from_object('config')
# app.json_encoder = CustomJSONEncoder  
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
db = SQLAlchemy()


def create_app(configFile):
    app = Flask(__name__)
    app.config.from_object(configFile)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

