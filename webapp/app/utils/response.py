from flask import jsonify

from .code import Code


def make_response(data=None, **kwargs):
    """
    封装jsonify
    :param data: 响应内容
    :param kwargs: 响应code以及msg
    :return:
    """
    code = kwargs.pop("code", Code.SUCCESS)
    msg = kwargs.pop("msg", Code.msg[code])
    res_data = {
        "code": code,
        "msg": msg,
        "data": data if data else [],
    }
    return jsonify(res_data), code
