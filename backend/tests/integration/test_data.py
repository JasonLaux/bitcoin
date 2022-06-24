import csv
from urllib import response
from crawler.exchange_data_etl import insert_exchange_data
from decimal import Decimal
from models import Exchange
import datetime

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
		with app.test_client() as client:
			response = client.get('/')
			# print(response.data)
		# 	print(222222222222222)
		# print(2222222)
		# with app.test_client() as client:
		# 	print(11111)
		# 	response = client.get('/')
		# 	print(response.data)
	expected_result = [
			{
				'id': 'binance',
				'name': 'Binance',
				'rank': 1,
				'percentTotalVolume': Decimal('25.44443'),
				'volumeUsd': Decimal('12712561147.7913049212358699'),
				'tradingPairs': 650,
				'socket': True,
				'exchangeUrl': 'https://www.binance.com/',
				'updated_unix_millis': 1625787943298,
				'updated_utc': datetime.datetime(
					2021, 7, 8, 23, 45, 43, 298000
				),
			},
			{
				'id': 'zg',
				'name': 'ZG.com',
				'rank': 2,
				'percentTotalVolume': Decimal('13.03445'),
				'volumeUsd': Decimal('6512276458.5226475820074930'),
				'tradingPairs': 133,
				'socket': False,
				'exchangeUrl': 'https://api.zg.com/',
				'updated_unix_millis': 1625787941554,
				'updated_utc': datetime.datetime(
					2021, 7, 8, 23, 45, 41, 554000
				),
			},
			{
				'id': 'huobi',
				'name': 'Huobi',
				'rank': 3,
				'percentTotalVolume': Decimal('5.93652'),
				'volumeUsd': Decimal('2966009471.8337660651992927'),
				'tradingPairs': 589,
				'socket': True,
				'exchangeUrl': 'https://www.hbg.com/',
				'updated_unix_millis': 1625787943276,
				'updated_utc': datetime.datetime(
					2021, 7, 8, 23, 45, 43, 276000
				),
			},
			{
				'id': 'okex',
				'name': 'Okex',
				'rank': 4,
				'percentTotalVolume': Decimal('4.99990'),
				'volumeUsd': Decimal('2498051785.3601278924449889'),
				'tradingPairs': 287,
				'socket': False,
				'exchangeUrl': 'https://www.okex.com/',
				'updated_unix_millis': 1625787941641,
				'updated_utc': datetime.datetime(
					2021, 7, 8, 23, 45, 41, 641000
				),
			},
		]
	# assert expected_result == response.data

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

