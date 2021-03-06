from flask import Flask

from app.handler.error_handler import error_handler_init
from conf.config import config
from app.utils.log import logger_init


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from . import models
    models.init_app(app)

    from app.api import v1
    v1.init_app(app)

    logger_init(app.config["APP_DIR"])
    error_handler_init(app)

    return app
