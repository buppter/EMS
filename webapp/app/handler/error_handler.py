import logging
import traceback

from app.utils.code import Code
from app.utils.response import make_response


def not_found(e):
    return make_response(code=Code.NOT_FOUND, msg=e.description)


def method_not_allowed(e):
    return make_response(code=Code.NOT_ALLOWED)


def bad_request(e):
    return make_response(code=Code.BAD_REQUEST, msg=e.description)


def server_error(e):
    logging.error("server error: %s" % traceback.format_exc())
    return make_response(code=Code.SERVER_ERROR)


def unsupported(e):
    return make_response(code=Code.UNSUPPORTED, msg=e.description)


def forbidden(e):
    return make_response(code=Code.FORBIDDEN, msg=e.description)


def error_handler_init(app):
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(415, unsupported)
    app.register_error_handler(500, server_error)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(403, forbidden)
