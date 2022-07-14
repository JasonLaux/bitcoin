from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(configFile):
    app = Flask(__name__, static_folder='../build', static_url_path='/')
    app.config.from_object(configFile)
    CORS(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app



