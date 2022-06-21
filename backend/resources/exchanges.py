from flask_restful import Resource
from models.exchange import Exchange

class Exchanges(Resource):

    def __init__(self) -> None:
        super().__init__()

    def get(self):

        return Exchange.query.all()