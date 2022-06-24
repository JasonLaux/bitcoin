class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ljx598923118@localhost:5432/postgres"

class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ljx598923118@localhost:5432/postgres"
    pass

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:ljx598923118@localhost:5432/postgres"

    @property
    def TESTINGORNOT(self):
        return self.TESTING