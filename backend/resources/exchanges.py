from flask_restful import Resource
# from flask_restful import marshal_with, fields
from models import Exchange
from crawler.exchange_data_etl import get_utc_from_unix_time
from marshmallow import Schema, fields, post_load
from flask import after_this_request

# resource_fields = {
#     'id': fields.String,
#     'name': fields.String,
#     'rank': fields.Integer,
#     'percentTotalVolume': fields.Float,
#     'volumeUsd': fields.Float,
#     'tradingPairs': fields.Integer,
#     'socket': fields.Boolean,
#     'exchangeUrl': fields.String,
#     'updated_unix_millis': fields.Integer,
#     'updated_utc': fields.DateTime(dt_format='iso8601')
# }


class ExchangeSchema(Schema):

    # Decimal cannot be serialized ??? then why provide fields.Decimal
    id = fields.String()
    name = fields.String()
    rank = fields.Integer()
    percentTotalVolume = fields.Float()
    volumeUsd = fields.Float()
    tradingPairs = fields.Integer()
    socket = fields.Boolean()
    exchangeUrl = fields.String()
    updated_unix_millis = fields.Integer()
    updated_utc = fields.DateTime(metadata={'dt_format':'iso8601'})

    @post_load
    def make_exchange(self, data, **kwargs):
        return Exchange(**data)

schema = ExchangeSchema(many=True)

class Exchanges(Resource):

    def __init__(self) -> None:
        
        super().__init__()

        # with current_app.app_context():
        #     insert_exchange_data()

    # @marshal_with(resource_fields, envelope='data')
    # @marshal_with(resource_fields)
    def get(self):
        @after_this_request
        def add_header(response):
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            return response
        # assert len(Exchange.query.all()) == 1
        # print(Exchange.query.get('binance'))
        return schema.dump(Exchange.query.all())
        # return {'test': 1}
        # return Exchange.query.all()


    # # for test purpose
    # def post(self):
    #     print("POSTING...")
    #     args = parser.parse_args()
    #     try:
    #         args['updated_utc'] = get_utc_from_unix_time(args['updated_unix_millis'])
    #         print(args)
    #         Exchange.add_one_exchange(args)
    #     except Exception as e:
    #         return {"message": f'Failed to insert data with error {e}'}, 400

    #     return {"message": f'Successfully create new exchange data with id'}, 201

