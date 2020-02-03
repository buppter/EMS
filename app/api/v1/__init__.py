from .org import org_bp


def init_app(app):
    app.register_blueprint(org_bp, url_prefix="/v1")
