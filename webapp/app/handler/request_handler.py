import logging

from werkzeug.exceptions import abort

from app.models.department import Department


def request_args_handler(request):
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 0)
    limit = request.args.get("limit", 0)
    offset = request.args.get("offset", 0)
    return page, per_page, limit, offset


def department_data_handler(request):
    data = request.get_json()
    if not data:
        logging.warning("data handler warning: 数据格式不正确，应该json格式")
        abort(415, description="数据应该为json格式")
    name = data.get("name")

    if Department.query.filter(Department.name == name).first():
        logging.warning("data handler warning: 该部门已存在")
        abort(400, description="该部门已存在")

    parent = data.get("parent")
    if not (name and parent):
        logging.warning("data handler warning: 数据不完整")
        abort(400, description="数据不完整")
    parent_node = Department.query.filter(Department.name == parent).first_or_400(description="所输入的parent不存在")

    return name, parent_node


def emp_data_handler(request):
    data = request.get_json()
    if not data:
        logging.warning("data handler warning: 数据格式不正确，应该json格式")
        abort(415, description="数据应该为json格式")
    name = data.get("name")
    gender = data.get("gender")
    department = data.get("department")

    # employee 无需判断 name 是否存在，所以在 model 设计里， Employee 的 name 字段不是 unique
    if not (name and gender and department):
        logging.warning("data handler warning: 数据不完整")
        abort(400, description="数据不完整")
    department = Department.query.filter(Department.name == department).first_or_400(description="所输入的department不存在")

    return name, gender, department
