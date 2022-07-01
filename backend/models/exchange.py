from dataclasses import dataclass
import datetime
from typing import Dict, List
from app import db
# migrate = Migrate(app, db)

@dataclass
class Exchange(db.Model):
    __tablename__ = 'exchange'
    # __table_args__ = {'extend_existing': True}

    id: str
    name: str
    rank: int
    percentTotalVolume: float
    volumeUsd: float
    tradingPairs: int
    socket: bool
    exchangeUrl: str
    updated_unix_millis: int
    updated_utc: datetime.datetime

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    percentTotalVolume = db.Column(db.Numeric(8, 5), nullable=True)
    volumeUsd = db.Column(db.Numeric, nullable=True)
    tradingPairs = db.Column(db.Integer, nullable=True)
    socket = db.Column(db.Boolean, nullable=True)
    exchangeUrl = db.Column(db.String(50), nullable=True)
    updated_unix_millis = db.Column(db.BigInteger, nullable=True)
    updated_utc = db.Column(db.DateTime, nullable=True)

    def __eq__(self, other):
        return other.id == self.id and \
                other.name == self.name and \
                other.rank == self.rank and \
                other.percentTotalVolume == self.percentTotalVolume and \
                other.volumeUsd == self.volumeUsd and \
                other.tradingPairs == self.tradingPairs and \
                other.socket == self.socket and \
                other.exchangeUrl == self.exchangeUrl and \
                other.updated_unix_millis == self.updated_unix_millis and \
                other.updated_utc == self.updated_utc 


    # def __repr__(self):
    #     return f'id: {self.id}, updated_time: {self.updated_utc}'

    def get_all_exchanges(self):
        return Exchange.query.all()
    
    def get_one_exchange(self, name: str):
        return Exchange.query.get(name)

    @staticmethod
    def add_one_exchange(instance: Dict) -> None:
        print(111111111111)
        print(instance)
        exchange = Exchange(**instance)
        db.session.add(exchange)
        db.session.commit()
    
    @staticmethod
    def add_all_exchanges(instances: List['Exchange'] ) -> None:
        db.session.add_all(instances)
        db.session.commit()


    
    

    