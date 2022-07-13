import os
class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DB_USER = os.environ['POSTGRES_USER']
    DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
    DB_DB = os.environ['POSTGRES_DB']
    DB_HOST = os.environ['POSTGRES_HOST']
    DB_PORT = os.environ['POSTGRES_PORT']

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ljx598923118@localhost:5432/postgres"

class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ljx598923118@localhost:5432/postgres"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_DB}"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ljx598923118@localhost:5432/postgres"

    @property
    def TESTINGORNOT(self):
        return self.TESTING