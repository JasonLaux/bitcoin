import pytest
from app import create_app, db
from config import TestingConfig
from decimal import Decimal
import datetime
from resources import Exchanges
from flask_restful import Api


@pytest.fixture()
def app():

    app = create_app(TestingConfig())
    assert app.config["TESTING"] == True

    api = Api(app)
    api.add_resource(Exchanges, '/')  

    # Initialize database
    
    yield app

    with app.app_context():
        print("terminate the app...")
        # clean up / reset resources here
        db.session.remove() # necessary for container from "https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/"
        db.drop_all()

# @pytest.fixture()
# def client(app):
#     return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()

# Test Cases
expected_result = [
            {
                'id': 'binance',
                'name': 'Binance',
                'rank': 1,
                'percenttotalvolume': Decimal('25.44443'),
                'volumeusd': Decimal('12712561147.7913049212358699'),
                'tradingpairs': 650,
                'socket': True,
                'exchangeurl': 'https://www.binance.com/',
                'updated_unix_millis': 1625787943298,
                'updated_utc': datetime.datetime(
                    2021, 7, 8, 23, 45, 43, 298000
                ),
            },
            {
                'id': 'zg',
                'name': 'ZG.com',
                'rank': 2,
                'percenttotalvolume': Decimal('13.03445'),
                'volumeusd': Decimal('6512276458.5226475820074930'),
                'tradingpairs': 133,
                'socket': False,
                'exchangeurl': 'https://api.zg.com/',
                'updated_unix_millis': 1625787941554,
                'updated_utc': datetime.datetime(
                    2021, 7, 8, 23, 45, 41, 554000
                ),
            },
            {
                'id': 'huobi',
                'name': 'Huobi',
                'rank': 3,
                'percenttotalvolume': Decimal('5.93652'),
                'volumeusd': Decimal('2966009471.8337660651992927'),
                'tradingpairs': 589,
                'socket': True,
                'exchangeurl': 'https://www.hbg.com/',
                'updated_unix_millis': 1625787943276,
                'updated_utc': datetime.datetime(
                    2021, 7, 8, 23, 45, 43, 276000
                ),
            },
            {
                'id': 'okex',
                'name': 'Okex',
                'rank': 4,
                'percenttotalvolume': Decimal('4.99990'),
                'volumeusd': Decimal('2498051785.3601278924449889'),
                'tradingpairs': 287,
                'socket': False,
                'exchangeurl': 'https://www.okex.com/',
                'updated_unix_millis': 1625787941641,
                'updated_utc': datetime.datetime(
                    2021, 7, 8, 23, 45, 41, 641000
                ),
            },
        ]