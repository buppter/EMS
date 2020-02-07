from .base import db
from flask_migrate import Migrate


def init_app(app):
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
