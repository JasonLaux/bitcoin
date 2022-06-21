from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
db = SQLAlchemy()
# migrate = Migrate(app, db)

@dataclass
class Exchange(db.Model):
    __tablename__ = 'exchange'
    __table_args__ = {"schema": "bitcoin"}

    id: str
    name: str
    rank: int
    percentTotalVolume: float
    volumeUsd: float
    tradingPairs: int
    socket: bool
    exchangeUrl: str
    updated_unix_millis: int
    updated_utc: str

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
    

    