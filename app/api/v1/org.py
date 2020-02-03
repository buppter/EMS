from flask import Blueprint, request

from app.libs.code import Code
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

    return make_response(data)


@org_bp.route("/org/<int:org_id>", methods=["GET"])
def get_org(org_id):
    """
    获取单个组织
    :param org_id: 部门id
    :return:
    """
    org = Node.query.get_or_404(org_id)
    return make_response(data=org.to_dict())


@org_bp.route("/orgs", methods=["POST"])
def post_org():
    """
    添加部门
    json格式{"name":"xxx", "ancestor": "xx"}
    :return:
    """
    data = request.get_json()
    if not data:
        return make_response(data=None, code=Code.BAD_REQUEST)
    name = data.get("name")
    ancestor = data.get("ancestor")
    if not (name and ancestor):
        return make_response(data=None, code=Code.BAD_REQUEST)

    ancestor_node = Node.query.filter(Node.name == ancestor).first_or_400()
    new_org = Node(name=name, ancestor=ancestor_node)
    try:
        db.session.add(new_org)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return make_response(data=None, code=Code.BAD_REQUEST)

    return make_response(data=None, code=Code.CREATED)


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
#     # all_orgs = OrgRelation.get(filter=[OrgRelation.ancestor_id == root_id, OrgRelation.distance > 0], order_by=OrgRelation.distance)
#     all_orgs = OrgRelation.get(filter=[OrgRelation.ancestor_id == org_id], order_by=OrgRelation.ancestor_id, page=page,
#                                per_page=per_page)
#     print(all_orgs)
#     return jsonify({"data": "hello world"}), 404

@org_bp.errorhandler(404)
def error404(e):
    return make_response(data=None, code=Code.NOT_FOUND)


@org_bp.errorhandler(400)
def bad_request(e):
    return make_response(data=None, code=Code.BAD_REQUEST)
