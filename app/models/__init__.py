from .models import db


def init_app(app):
    db.init_app(app)
