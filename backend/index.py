from app import create_app
from flask_restful import Api
from resources import Exchanges
import os
from apscheduler.schedulers.background import BackgroundScheduler
from crawler.exchange_data_etl import insert_exchange_data
from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer

load_dotenv()

scheduler = BackgroundScheduler(daemon=True)

if os.environ["FLASK_ENV"] == "development":
    print("Development mode...")
    configFile = 'config.DevelopmentConfig'
elif os.environ["FLASK_ENV"] == "production":
    print("Procution mode...")
    configFile = 'config.ProductionConfig'

app = create_app(configFile)
# Routing
api = Api(app)
api.add_resource(Exchanges, '/api/exchange') 

def schedule_insert_exchange_data():
    with app.app_context():
        insert_exchange_data()

scheduler.add_job(func=schedule_insert_exchange_data, trigger="interval", minutes=60)

@app.before_first_request
def initialize():
    print(1111111111111111)
    insert_exchange_data()
    scheduler.start()

@app.route('/')
def index():
    return app.send_static_file('index.html')


# @app.after_request
# def add_header(response):
#     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

if __name__ == '__main__':
    wsgi_server = WSGIServer(("0.0.0.0", 3000), app)
    wsgi_server.serve_forever()
    # atexit.register(lambda: scheduler.shutdown())

# with app.app_context():
#     print("disconnect database and clear data...2")
#     db.session.remove()
#     db.drop_all()


# if __name__ == '__main__':
#     run()