import logging

from werkzeug.exceptions import abort

from app.models.organization import Node


def request_args_handler(request):
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 0)
    limit = request.args.get("limit", 0)
    offset = request.args.get("offset", 0)
    return page, per_page, limit, offset


def org_data_handler(request):
    data = request.get_json()
    if not data:
        logging.warning("data handler warning: 数据格式不正确，应该json格式")
        abort(415, description="数据应该为json格式")
    name = data.get("name")

    if Node.query.filter(Node.name == name).first():
        logging.warning("data handler warning: 该部门已存在")
        abort(400, description="该部门已存在")

    ancestor = data.get("ancestor")
    if not (name and ancestor):
        logging.warning("data handler warning: 数据不完整")
        abort(400, description="数据不完整")
    ancestor_node = Node.query.filter(Node.name == ancestor).first_or_400(description="所输入的ancestor不存在")

    return name, ancestor_node


def emp_data_handler(request):
    data = request.get_json()
    if not data:
        logging.warning("data handler warning: 数据格式不正确，应该json格式")
        abort(415, description="数据应该为json格式")
    name = data.get("name")
    gender = data.get("gender")
    org = data.get("org")

    # employee 无需判断 name 是否存在，所以在 model 设计里， Employee 的 name 字段不是 unique
    if not (name and gender and org):
        logging.warning("data handler warning: 数据不完整")
        abort(400, description="数据不完整")
    org = Node.query.filter(Node.name == org).first_or_400(description="所输入的org不存在")

    return name, gender, org
