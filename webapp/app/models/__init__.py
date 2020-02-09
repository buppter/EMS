from .base import db
from flask_migrate import Migrate
from app.models.organization import Node
from app.models.employee import Employee


def init_app(app):
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
