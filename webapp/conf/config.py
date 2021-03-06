import os

from conf import secure


class Config:
    SECRET_KEY = secure.SECRET_KEY
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = secure.DEV_SQLALCHEMY_DATABASE_URI
    REDIS_URL = secure.DEV_REDIS_URL


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = secure.TEST_SQLALCHEMY_DATABASE_URI
    REDIS_URL = secure.TEST_REDIS_URL


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = secure.PROD__SQLALCHEMY_DATABASE_URI
    REDIS_URL = secure.PROD_REDIS_URL


config = {
    "development": DevelopmentConfig,
    "test": TestConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

PER_PAGE_NUM = 20

LIMIT_MAX_TOKEN = 10

LIMIT_TOKEN_RATE = 10

REDIS_KEY_PREFIX = "limit_rate::remote_id::"
