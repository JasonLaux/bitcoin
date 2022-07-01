from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(configFile):
    app = Flask(__name__)
    app.config.from_object(configFile)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app



