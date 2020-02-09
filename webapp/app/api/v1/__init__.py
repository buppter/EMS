from .org import org_bp
from .emp import emp_bp


def init_app(app):
    app.register_blueprint(org_bp, url_prefix="/v1")
    app.register_blueprint(emp_bp, url_prefix="/v1")
