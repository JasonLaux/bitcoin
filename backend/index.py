from time import sleep
from app import create_app, db
from flask_restful import Api
from resources import Exchanges
import os
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from crawler.exchange_data_etl import insert_exchange_data

scheduler = BackgroundScheduler(daemon=True)

os.environ["FLASK_ENV"] = "development"
app = create_app('config.DevelopmentConfig')

# Routing
api = Api(app)
api.add_resource(Exchanges, '/api/exchange') 

def schedule_insert_exchange_data():
    with app.app_context():
        insert_exchange_data()

scheduler.add_job(func=schedule_insert_exchange_data, trigger="interval", minutes=60)

@app.before_first_request
def initialize():
    insert_exchange_data()
    scheduler.start()


# @app.after_request
# def add_header(response):
#     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

if __name__ == '__main__':
    app.run(debug=True)
    # atexit.register(lambda: scheduler.shutdown())

# with app.app_context():
#     print("disconnect database and clear data...2")
#     db.session.remove()
#     db.drop_all()


# if __name__ == '__main__':
#     run()