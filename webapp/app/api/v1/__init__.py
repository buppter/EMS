from .department import department_bp
from .employee import employee_bp


def init_app(app):
    app.register_blueprint(department_bp, url_prefix="/v1")
    app.register_blueprint(employee_bp, url_prefix="/v1")
