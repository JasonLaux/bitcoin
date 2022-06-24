import csv
from curses import meta
from urllib import response
from crawler.exchange_data_etl import insert_exchange_data
from decimal import Decimal
from models import Exchange
import datetime
from crawler.exchange_data_etl import get_utc_from_unix_time

def test_insert_exchange_data(app, mocker):

	mocker.patch(
		'crawler.exchange_data_etl.get_exchange_data',
		return_value=[
			r
			for r in csv.DictReader(
				open('tests/fixtures/sample_raw_exchange_data.csv')
			)
		],
	)

	with app.app_context():
		insert_exchange_data()
		# with app.test_client() as client:
		# 	response = client.get('/')
			# print(response.data)
		# print(2222222)
		# with app.test_client() as client:
		# 	print(11111)
		# 	response = client.get('/')
		# 	print(response.data)

		meta_data = {
					'id': 'binance',
					'name': 'Binance',
					'rank': 1,
					'percentTotalVolume': Decimal('25.44443'),
					'volumeUsd': Decimal('12712561147.7913049212358699'),
					'tradingPairs': 650,
					'socket': True,
					'exchangeUrl': 'https://www.binance.com/',
					'updated_unix_millis': 1625787943298,
				}
		meta_data['updated_utc'] = get_utc_from_unix_time(meta_data.get('updated_unix_millis'))
		test_exchange = Exchange(**meta_data)
		assert test_exchange == Exchange.query.all()[0]

    # assert 'success' in data['status']


    # def test_get_exchange_data(self, mocker):

    #     """
    #     GIVEN a Flask application configured for testing
    #     WHEN the '/' page is requested (GET)
    #     THEN check that the response is valid
    #     """

    #     # mocker.patch(
    #     #     'crawler.exchange_data_etl.get_exchange_data',
    #     #     return_value=[
    #     #         r
    #     #         for r in csv.DictReader(
    #     #             open('tests/fixtures/sample_raw_exchange_data.csv')
    #     #         )
    #     #     ],
    #     # )

    #     response = client.get('/')

    #     assert response.status_code == 200
    #     assert response.data == expected_result 

