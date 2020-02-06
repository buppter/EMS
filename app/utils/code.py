class Code:
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_FOUND = 404
    BAD_REQUEST = 400
    UNSUPPORTED = 415
    SERVER_ERROR = 500
    NOT_ALLOWED = 405
    FORBIDDEN = 403

    msg = {
        SUCCESS: "success",
        CREATED: "created",
        NO_CONTENT: "no content",
        NOT_FOUND: "not found",
        BAD_REQUEST: "bad request",
        SERVER_ERROR: "server error",
        UNSUPPORTED: "unsupported media type",
        NOT_ALLOWED: "method not allowed",
        FORBIDDEN: "forbidden"
    }
