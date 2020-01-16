from flask import Flask

from conf.config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from . import models
    models.init_app(app)

    from app.api import v1
    v1.init_app(app)

    return app
