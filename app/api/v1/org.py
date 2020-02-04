from flask import Blueprint, request, _request_ctx_stack

from app.libs.code import Code
from app.libs.handler import data_handler
from app.libs.response import make_response
from app.models import db
from app.models.organization import Node

org_bp = Blueprint("organization", __name__)


@org_bp.route("/orgs")
def all_node():
    """
    获取完整的组织列表
    :return:
    """
    node = Node.get_root()
    data = node.dumps()

    return make_response(data=data)


@org_bp.route("/org/<int:org_id>", methods=["GET", "PUT", "DELETE"])
def get_org(org_id):
    """
    获取或更新单个组织
    :param org_id: 部门id
    :return:
    """
    org = Node.query.get_or_404(org_id)
    if request.method == "GET":
        return make_response(data=org.to_dict())

    if request.method == "PUT":
        name, ancestor = data_handler(request)
        org.name = name
        org.ancestor = ancestor
        with db.auto_commit():
            db.session.add(org)
        return make_response()

    if request.method == "DELETE":
        with db.auto_commit():
            db.session.delete(org)
        return make_response()


@org_bp.route("/orgs", methods=["POST"])
def create_org():
    """
    添加部门
    post的数据为json格式
    示例：{"name":"xxx", "ancestor": "xx"}
    :return:
    """
    name, ancestor = data_handler(request)
    if Node.query.filter(Node.name == name).first():
        return make_response(code=Code.BAD_REQUEST, msg="该部门已存在")

    new_org = Node(name=name, ancestor=ancestor)
    with db.auto_commit():
        db.session.add(new_org)

    return make_response(code=Code.CREATED)


#
# @org_bp.route("/orgs/<int:id>")
# def node(id):
#     page = request.args.get("page", 0)
#     per_page = request.args.get("per_page", 0)
#     limit = request.args.get("limit", 0)
#     offset = request.args.get("offset", 0)
#     order_by = request.args.get("order_by", None)
#     org = request.args.get("org", None)
#
#     org_id = Organization.root()
#     if org is not None:
#         org = Organization.get(filter=[Organization.name == org], first=True)
#         # root = simple_select(table_class=OrgRelation, order_by=OrgRelation.distance.desc(), first=True)
#
#         if org:
#             org_id = org.id
#         else:
#             raise Exception("输入的组织名称不存在")
#
#     return jsonify({"data": "hello world"}), 404

@org_bp.errorhandler(404)
def error404(e):
    return make_response(code=Code.NOT_FOUND)


@org_bp.errorhandler(400)
def bad_request(e):
    return make_response(code=Code.BAD_REQUEST, msg=e.description)


@org_bp.errorhandler(500)
def bad_request(e):
    return make_response(code=Code.SERVER_ERROR)


@org_bp.errorhandler(415)
def bad_request(e):
    return make_response(code=Code.UNSUPPORTED, msg=e.description)
