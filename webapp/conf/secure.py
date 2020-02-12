import os

SECRET_KEY = "employee management system"

"""
============DEV CONFIG============
"""
DEV_SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/ems'

DEV_REDIS_URL = {
    "HOST": os.getenv("HOST"),
    "PORT": 6379,
    "PASSWORD": os.getenv("REDIS_AUTH"),
}

"""
============TEST CONFIG============
"""
TEST_SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/test'

TEST_REDIS_URL = {
    "HOST": "47.105.204.183",
    "PORT": 6379,
    "PASSWORD": "THzhiku",
}

"""
============PROD CONFIG============
"""

PROD__SQLALCHEMY_DATABASE_URI = "mysql://root:123456@{}:3306/ems".format("mysql")
PROD_REDIS_URL = {
    "HOST": "redis",
    "PORT": 6379
}
