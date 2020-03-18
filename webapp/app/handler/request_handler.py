import logging

from werkzeug.exceptions import abort

from app.models.department import Department
from app.utils.gender import gender_to_num

"""
封装一些请求的数据处理方法
"""


def request_args_handler(request):
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 0)
    limit = request.args.get("limit", 0)
    offset = request.args.get("offset", 0)
    return page, per_page, limit, offset


def department_request_handler(request, department=None):
    data = request.get_json()
    if not data:
        logging.warning("data handler warning: 数据格式不正确，应该json格式")
        abort(415, description="数据应该为json格式")
    name = data.get("name")
    parent = data.get("parent")
    if not (name and parent):
        logging.warning("data handler warning: 数据不完整")
        abort(400, description="请求数据不完整")
    # 判断 name 是否重复
    if request.method == "POST" or (department and department.name != name):
        # POST 方法下，如果 name 已存在，则 abort
        # PUT 方法下，如果 PUT 的数据，更新了 name 字段，则需要判断 name 是否已存在
        # 如果更新的对象 name 不变，而更新的是其他信息，这时候不需要判断 name 是都已存在
        if Department.query.filter_by(name=name).first():
            logging.warning("data handler warning: 该部门已存在")
            abort(400, description="该部门已存在")

    parent_node = Department.query.filter_by(name=parent).first_or_400(description="所输入的parent不存在")

    return name, parent_node.id


def employee_request_handler(request):
    data = request.get_json()
    if not data:
        logging.warning("data handler warning: 数据格式不正确，应该json格式")
        abort(415, description="请求数据应该为json格式")
    name = data.get("name")
    gender = data.get("gender")
    department = data.get("department")

    # employee 无需判断 name 是否存在，所以在 model 设计里， Employee 的 name 字段不是 unique
    if not (name and gender and department):
        logging.warning("data handler warning: 数据不完整")
        abort(400, description="请求数据不完整")
    department = Department.query.filter_by(name=department).first_or_400(description="所输入的department不存在")

    return name, gender, department


def employees_filed_handler(request):
    fields = {}
    exists = False
    gender = request.args.get("gender")
    gender = gender_to_num(gender) if gender else None
    if gender is not None:
        fields.update({"_gender": gender})
        exists = True

    department = request.args.get("department")
    if department:
        department = Department.query.filter_by(name=department).first_or_404(
            description="所查询的department不存在")
    if department:
        fields.update({"department_id": department.id})

    name = request.args.get("name")
    if name:
        fields.update({"name": name})
        exists = True
    return fields, exists
