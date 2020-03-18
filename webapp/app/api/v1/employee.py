import logging
import traceback
from werkzeug.exceptions import abort

from flask import Blueprint, request

from app.handler.request_handler import request_args_handler, employee_request_handler, employees_filed_handler
from app.models import Employee, db
from app.utils.code import Code
from app.utils.rate_limiter import limit_rate
from app.utils.query import select
from app.utils.response import make_response

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees", methods=["GET", "POST"])
@limit_rate()
def employees():
    """
    获取员工列表，添加新员工
    支持query参数：name, gender, department, limit, offset, page, per_page
    :return:
    """
    if request.method == "GET":
        page, per_page, limit, offset = request_args_handler(request)
        fields, exists = employees_filed_handler(request)
        employees_list = select(Employee, filter=fields, page=page, per_page=per_page, limit=limit, offset=offset,
                                exists=exists)
        data = [employee.dumps() for employee in employees_list]

        return make_response(data=data)

    if request.method == "POST":
        name, gender, department = employee_request_handler(request)
        new_employee = Employee(name=name, gender=gender, department_id=department.id)
        with db.auto_commit():
            db.session.add(new_employee)
        logging.info("create a new employee: %s" % new_employee.dumps())
        return make_response(data=new_employee.dumps(), code=Code.CREATED)


@employee_bp.route("/employees/<int:employee_id>", methods=["GET", "PUT", "DELETE"])
@limit_rate()
def single_emp(employee_id):
    """
    根据员工id获取，更新，删除员工信息
    :param employee_id: 员工ID
    :return:
    """
    employee = Employee.query.filter_by(id=employee_id).first_or_404(description="所查询的员工ID不存在")
    if request.method == "GET":
        return make_response(data=employee.dumps())

    if request.method == "PUT":
        name, gender, department = employee_request_handler(request)
        old_employee_info = employee
        employee.name = name
        employee.gender = gender
        employee.department_id = department.id

        try:
            db.session.commit()
        except Exception:
            logging.error(
                "update employee error, employee info: %s, old employee info: %s. \n traceback error: %s" % (
                    employee.dumps(), old_employee_info.dumps(), traceback.format_exc()))
            abort(500)
        logging.info(
            "update a employee info: %s, before update the employee info: %s" % (
                employee.dumps(), old_employee_info.dumps()))
        return make_response(data=employee.dumps())

    if request.method == "DELETE":
        with db.auto_commit():
            employee.delete()
        return make_response()
