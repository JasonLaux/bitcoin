from app import create_app
from flask_restful import Api
from resources import Exchanges
import os

os.environ["FLASK_ENV"] = "development"

def run():
    app = create_app('config.DevelopmentConfig')
    print(app.config["TESTING"])

    # Routing
    api = Api(app)
    api.add_resource(Exchanges, '/')    
    
    app.run(debug=True)

if __name__ == '__main__':
    run()