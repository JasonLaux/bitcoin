from app import create_app, db
from flask_restful import Api
from resources import Exchanges
import os

os.environ["FLASK_ENV"] = "development"
app = create_app('config.DevelopmentConfig')

# Routing
api = Api(app)
api.add_resource(Exchanges, '/api/exchange') 

@app.before_first_request
def initialize():
    from crawler.exchange_data_etl import insert_exchange_data
    insert_exchange_data()

@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

app.run(debug=True)

with app.app_context():
    print("disconnect database and clear data...2")
    db.session.remove()
    db.drop_all()


# if __name__ == '__main__':
#     run()