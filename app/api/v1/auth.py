from flask import Blueprint

from app.models.models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth", methods=["post"])
def get_token():
    user = User.query.filter_by()