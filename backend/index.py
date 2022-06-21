from app import create_app
from flask_restful import Api
from resources import Exchanges
from models.exchange import db


def run():
    app = create_app()

    # Create all tables
    with app.app_context():
        db.create_all()

    # Routing
    api = Api(app)
    api.add_resource(Exchanges, '/')    
    
    app.run(debug=True)