import logging
import traceback
from werkzeug.exceptions import abort

from flask import Blueprint, request

from app.handler.request_handler import request_args_handler, employee_data_handler
from app.models import Employee, Department, db
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

        fields = []
        exists = False
        gender = request.args.get("gender")
        gender_dic = {"男": 1, "女": 0}
        gender = gender_dic.get(gender)
        if gender is not None:
            fields.append(Employee._gender == gender)
            exists = True

        department = request.args.get("department")
        if department:
            department = Department.query.filter(Department.name == department).first_or_404(description="所查询的department不存在")
        if department:
            fields.append(Employee.department_id == department.id)

        name = request.args.get("name")
        if name:
            fields.append(Employee.name == name)
            exists = True

        emp_list = select(Employee, filter=fields, page=page, per_page=per_page, limit=limit, offset=offset,
                          exists=exists)
        data = [emp.dumps() for emp in emp_list]

        return make_response(data=data)

    if request.method == "POST":
        name, gender, department = employee_data_handler(request)
        new_emp = Employee(name=name, gender=gender, department_id=department.id)
        with db.auto_commit():
            db.session.add(new_emp)
        logging.info("create a new employee: %s" % new_emp.dumps())
        return make_response(code=Code.CREATED)


@employee_bp.route("/employees/<int:emp_id>", methods=["GET", "PUT", "DELETE"])
@limit_rate()
def single_emp(emp_id):
    """
    根据员工id获取，更新，删除员工信息
    :param emp_id: 员工ID
    :return:
    """
    emp = Employee.query.get_or_404(emp_id, description="所查询的员工ID不存在")
    if request.method == "GET":
        return make_response(data=emp.dumps())

    if request.method == "PUT":
        name, gender, department = employee_data_handler(request)
        old_emp = emp
        emp.name = name
        emp.gender = gender
        emp.department_id = department.id

        try:
            db.session.commit()
        except Exception:
            logging.error(
                "update employee error, employee info: %s, old employee info: %s. \n traceback error: %s" % (
                    emp.dumps(), old_emp.dumps(), traceback.format_exc()))
            abort(500)

        return make_response()

    if request.method == "DELETE":
        with db.auto_commit():
            db.session.delete(emp)
        return make_response()
