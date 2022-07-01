from app import create_app, db
from flask_restful import Api
from resources import Exchanges
import os

os.environ["FLASK_ENV"] = "development"
app = create_app('config.DevelopmentConfig')

# Routing
api = Api(app)
api.add_resource(Exchanges, '/') 

@app.before_first_request
def initialize():
    from crawler.exchange_data_etl import insert_exchange_data
    insert_exchange_data()

app.run(debug=True)

with app.app_context():
    print("disconnect database and clear data...2")
    db.session.remove()
    db.drop_all()


# if __name__ == '__main__':
#     run()