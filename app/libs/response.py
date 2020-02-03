from flask import jsonify

from .code import Code


# todo:后边要重构这部分
def make_response(data=None, code=Code.SUCCESS):
    data = {
        "code": code,
        "msg": Code.msg[code],
        "data": data if data else [],
    }
    return jsonify(data)


def get_code(data):
    if data is not None:
        code = Code.SUCCESS
    else:
        code = Code.NOT_FOUND

    return code
