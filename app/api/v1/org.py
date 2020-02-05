import logging

from flask import Blueprint, request

from app.utils.code import Code
from app.utils.handler import data_handler
from app.utils.response import make_response
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
    logging.info("get all org info: %s" % data)
    return make_response(data=data)


@org_bp.route("/orgs/<int:org_id>", methods=["GET", "PUT", "DELETE"])
def get_org(org_id):
    """
    获取、更新或删除单个部门组织
    :param org_id: 部门id
    :return:
    """
    org = Node.query.get_or_404(org_id)
    if request.method == "GET":
        logging.info("get a org info: %s" % org.to_dict())
        return make_response(data=org.to_dict())

    if request.method == "PUT":
        name, ancestor = data_handler(request)
        old_org_info = org
        org.name = name
        org.ancestor = ancestor
        with db.auto_commit():
            db.session.add(org)
        logging.info("update a org info: %s, before update the org info: %s" % (org, old_org_info))
        return make_response()

    if request.method == "DELETE":
        with db.auto_commit():
            db.session.delete(org)
        logging.info("delete a org: %s" % org)
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
        logging.warning(
            'create a org error: 该部门已存在, the create org info: {"name": %s, ancestor: %s}' % (name, ancestor.name))
        return make_response(code=Code.BAD_REQUEST, msg="该部门已存在")

    new_org = Node(name=name, ancestor=ancestor)
    with db.auto_commit():
        db.session.add(new_org)
    logging.info("create a new org: %s" % new_org.to_dict())
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

