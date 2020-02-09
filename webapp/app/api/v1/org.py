import logging
import traceback

from werkzeug.exceptions import abort
from flask import Blueprint, request

from app.utils.code import Code
from app.handler.request_handler import org_data_handler, request_args_handler
from app.utils.limit_rate import limit_rate
from app.utils.response import make_response
from app.utils.query import select
from app.models import db
from app.models.organization import Node

org_bp = Blueprint("organization", __name__)


@org_bp.route("/orgs")
@limit_rate()
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
@limit_rate()
def single_org(org_id):
    """
    获取、更新或删除单个部门组织
    :param org_id: 部门id
    :return:
    """
    org = Node.query.get_or_404(org_id, description="部门ID不存在")
    if request.method == "GET":
        logging.info("get a org info: %s" % org.to_dict())
        return make_response(data=org.to_dict())

    if request.method == "PUT":
        name, ancestor = org_data_handler(request)
        old_org_info = org
        org.name = name
        org.ancestor = ancestor
        try:
            db.session.commit()
        except Exception:
            logging.error(
                "update org error, org info: %s, old org info: %s. \n traceback error: %s" % (
                    org.to_dict(), old_org_info.to_dict(), traceback.format_exc()))
            abort(500)
        logging.info("update a org info: %s, before update the org info: %s" % (org, old_org_info))
        return make_response()

    if request.method == "DELETE":
        with db.auto_commit():
            db.session.delete(org)
        logging.info("delete a org: %s" % org)
        return make_response()


@org_bp.route("/orgs", methods=["POST"])
@limit_rate()
def create_org():
    """
    添加部门
    post的数据为json格式
    示例：{"name":"xxx", "ancestor": "xx"}
    :return:
    """
    name, ancestor = org_data_handler(request)
    new_org = Node(name=name, ancestor=ancestor)
    with db.auto_commit():
        db.session.add(new_org)
    logging.info("create a new org: %s" % new_org.to_dict())
    return make_response(code=Code.CREATED)


@org_bp.route("/orgs/ancestor/<int:org_id>", methods=["GET"])
@limit_rate()
def get_ancestor(org_id):
    """
    获取某一部门的上级部门
    :param org_id: 部门ID
    :return:
    """
    org = Node.query.get_or_404(org_id, description="部门ID不存在")
    org_ancestor = Node.query.get_or_404(org.ancestor_id, description="部门不存在")
    logging.info("get the org: %s, its ancestor is: %s" % (org.to_dict(), org_ancestor.to_dict()))
    return make_response(data=org_ancestor.to_dict())


@org_bp.route("/orgs/subs/<int:org_id>", methods=["GET"])
@limit_rate()
def get_subs(org_id):
    """
    获取某一部门子部门
    :param org_id: 部门ID
    :return:
    """
    page, per_page, limit, offset = request_args_handler(request)
    org = Node.query.get_or_404(org_id, description="部门ID不存在")
    nodes = select(Node, filter=[Node.ancestor_id == org_id], page=page, per_page=per_page, limit=limit, offset=offset)
    data = [node.to_dict() for node in nodes]
    logging.info("get the subs of org(%s): %s" % (org.to_dict(), data))
    return make_response(data=data)
