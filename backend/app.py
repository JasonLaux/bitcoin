from flask import Flask
# from utils import CustomJSONEncoder
# app.config.from_object('config')
# app.json_encoder = CustomJSONEncoder  
from models.exchange import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    return app

