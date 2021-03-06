import logging
import traceback

from werkzeug.exceptions import abort
from flask import Blueprint, request

from app.utils.code import Code
from app.handler.request_handler import department_request_handler, request_args_handler
from app.utils.rate_limiter import limit_rate
from app.utils.response import make_response
from app.utils.query import select
from app.models import db
from app.models.department import Department

department_bp = Blueprint("department", __name__)


@department_bp.route("/departments")
@limit_rate()
def all_node():
    """
    获取完整的组织列表
    :return:
    """
    node = Department.get_root()
    data = {}
    for i in node:
        data.update(i.dumps_all())
    logging.info("get all department info: %s" % data)
    return make_response(data=[data])


@department_bp.route("/departments/<int:department_id>", methods=["GET", "PUT", "DELETE"])
@limit_rate()
def single_department(department_id):
    """
    获取、更新或删除单个部门组织
    :param department_id: 部门id
    :return:
    """
    department = Department.query.filter_by(id=department_id).first_or_404(description="部门ID不存在")
    if request.method == "GET":
        logging.info("get a department info: %s" % department.dumps())
        return make_response(data=department.dumps_detail())

    if request.method == "PUT":
        name, parent_id = department_request_handler(request, department)
        old_department_info = department
        department.name = name
        department.parent_id = parent_id
        try:
            db.session.commit()
        except Exception:
            logging.error(
                "update department error, department info: %s, old department info: %s. \n traceback error: %s" % (
                    department.dumps(), old_department_info.dumps(), traceback.format_exc()))
            abort(500)
        logging.info(
            "update a department info: %s, before update the department info: %s" % (
                department.dumps(), old_department_info.dumps()))
        return make_response(data=department.dumps_detail())

    if request.method == "DELETE":
        with db.auto_commit():
            department.delete()
        logging.info("delete a department: %s" % department)
        return make_response()


@department_bp.route("/departments", methods=["POST"])
@limit_rate()
def create_department():
    """
    添加部门
    post的数据为json格式
    示例：{"name":"xxx", "parent": "xx"}
    :return:
    """
    name, parent_id = department_request_handler(request)
    new_department = Department(name=name, parent_id=parent_id)
    with db.auto_commit():
        db.session.add(new_department)
    logging.info("create a new department: %s" % new_department.dumps())
    return make_response(data=new_department.dumps_detail(), code=Code.CREATED)


@department_bp.route("/departments/<int:department_id>/parent", methods=["GET"])
@limit_rate()
def get_parent(department_id):
    """
    获取某一部门的上级部门
    :param department_id: 部门ID
    :return:
    """
    department = Department.query.filter_by(id=department_id).first_or_404(description="部门ID不存在")
    department_parent = Department.query.filter_by(id=department.parent_id).first_or_404(description="该部门的上级部门不存在")
    logging.info("get the department: %s, its parent is: %s" % (department.dumps(), department_parent.dumps()))
    return make_response(data=department_parent.dumps())


@department_bp.route("/departments/<int:department_id>/subs", methods=["GET"])
@limit_rate()
def get_subs(department_id):
    """
    获取某一部门子部门
    :param department_id: 部门ID
    :return:
    """
    page, per_page, limit, offset = request_args_handler(request)
    department = Department.query.filter_by(id=department_id).first_or_404(description="部门ID不存在")
    nodes = select(Department, filter={"parent_id": department_id}, page=page, per_page=per_page,
                   limit=limit, offset=offset)
    data = [node.dumps() for node in nodes]
    logging.info("get the subs of department(%s): %s" % (department.dumps(), data))
    return make_response(data=data)


@department_bp.route("/departments/<int:department_id>/siblings", methods=["GET"])
@limit_rate()
def get_siblings(department_id):
    """
    获取部门的兄弟部门
    :param department_id: 部门ID
    :return:
    """
    page, per_page, limit, offset = request_args_handler(request)
    department = Department.query.filter_by(id=department_id).first_or_404(description="部门ID不存在")

    nodes = select(Department, filter=[Department.parent_id == department.parent_id, Department.id != department.id,
                                       Department.status == 1], page=page, per_page=per_page, limit=limit,
                   offset=offset)
    data = [node.dumps() for node in nodes]
    logging.info("get the siblings of department(%s): %s" % (department.dumps(), data))
    return make_response(data=data)
