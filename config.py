class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        "db": "OP",
        "host": "op-ticketing-mongo",
        "port": 27017,
    }
    RABBITMQ_HOST = "my_rabbitmq"
    RABBITMQ_QUEUE = "upload defects"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": "OP",
        "host": "op-ticketing-mongo",
        "port": 27017,
    }


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        "db": "test",
        "host": "mongomock://localhost",
        "port": 27017,
    }
