import functools
from flask import request, abort

from app.utils.redis_cli import Redis
from conf.config import LIMIT_RATE_NUM


def limit_rate(nums=LIMIT_RATE_NUM, time=60):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            n = Redis.get(request.remote_addr)
            if not n:
                Redis.setex(request.remote_addr, time, 0)
                n = 0
            if int(n) == nums:
                abort(403, description="API rate limit exceeded")
            Redis.incr(request.remote_addr)
            return func(*args, **kwargs)
        return wrapper
    return decorator
