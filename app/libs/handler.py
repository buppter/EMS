from werkzeug.exceptions import abort

from app.models.organization import Node


def data_handler(request):
    data = request.get_json()
    if not data:
        abort(415, description="数据应该为json格式")
    name = data.get("name")
    ancestor = data.get("ancestor")
    if not (name and ancestor):
        abort(400, description="数据不完整")
    ancestor_node = Node.query.filter(Node.name == ancestor).first_or_400(description="所输入的ancestor不存在")

    return name, ancestor_node
