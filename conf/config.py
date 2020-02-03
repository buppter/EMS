import os

from conf import secure


class Config:
    SECRET_KEY = secure.SECRET_KEY
    PER_PAGE_NUM = secure.PER_PAGE_NUM
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = secure.DEV_SQLALCHEMY_DATABASE_URI


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = secure.TEST_SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "test": TestConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
