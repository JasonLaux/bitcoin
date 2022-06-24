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
    percentTotalVolume = db.Column(db.Numeric(8, 5), nullable=False)
    volumeUsd = db.Column(db.Numeric, nullable=False)
    tradingPairs = db.Column(db.Integer, nullable=False)
    socket = db.Column(db.Boolean, nullable=False)
    exchangeUrl = db.Column(db.String(50), nullable=False)
    updated_unix_millis = db.Column(db.BigInteger, nullable=False)
    updated_utc = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'id: {self.id}, updated_time: {self.updated_utc}'

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


    
    

    