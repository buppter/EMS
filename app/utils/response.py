from flask import jsonify

from .code import Code


# todo:后边要重构这部分
def make_response(data=None, **kwargs):
    code = kwargs.pop("code", Code.SUCCESS)
    msg = kwargs.pop("msg", Code.msg[code])
    res_data = {
        "code": code,
        "msg": msg,
        "data": data if data else [],
    }
    return jsonify(res_data), code
