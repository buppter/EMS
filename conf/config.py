from conf import secure


class Config:
    SECRET_KEY = secure.SECRET_KEY
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = secure.DEV_SQLALCHEMY_DATABASE_URI
    REDIS_URL = secure.DEV_REDIS_URL


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = secure.TEST_SQLALCHEMY_DATABASE_URI
    REDIS_URL = secure.TEST_REDIS_URL


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = secure.DEV_SQLALCHEMY_DATABASE_URI


config = {
    "development": DevelopmentConfig,
    "test": TestConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

PER_PAGE_NUM = 2

LIMIT_RATE_NUM = 10

REDIS_KEY_PREFIX = "limit_rate::remote_id::"
