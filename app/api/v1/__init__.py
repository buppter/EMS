from .employee import emp_bp
from .org import org_bp
from .auth import auth_bp


def init_app(app):
    app.register_blueprint(emp_bp, url_prefix="/v1")
    app.register_blueprint(org_bp, url_prefix="/v1")
    app.register_blueprint(auth_bp, url_prefix="/v1")
