import functools
from flask import request, abort

from app.utils.redis_cli import Redis
from app.utils.time_millis import current_time_millis
from conf.config import LIMIT_TOKEN_RATE, LIMIT_MAX_TOKEN, REDIS_KEY_PREFIX

lua = """
local ratelimit_info = redis.pcall('HMGET',KEYS[1],'last_time','current_token')
local last_time = ratelimit_info[1]
local current_token = tonumber(ratelimit_info[2])
local max_token = tonumber(ARGV[1])
local token_rate = tonumber(ARGV[2])
local current_time = tonumber(ARGV[3])
local reverse_time = 1000/token_rate
if current_token == nil then
    current_token = max_token
    last_time = current_time
else
    local past_time = current_time - last_time
    local reverse_token = math.floor(past_time/reverse_time)
    current_token = current_token+reverse_token
    last_time = reverse_time * reverse_token + last_time
    if current_token>max_token then
        current_token = max_token
    end
end
local result = 0
if(current_token > 0) then
    result = 1
    current_token = current_token - 1
end
redis.call('HMSET',KEYS[1],'last_time',last_time,'current_token',current_token)
redis.call('expire',KEYS[1],math.ceil(reverse_time * (max_token - current_token) + (current_time - last_time)))
return result
"""


def is_limit(key, max_token, token_rate):
    cli = Redis.script(lua)
    res = cli(keys=key, args=[str(max_token), str(token_rate), str(current_time_millis())])
    return 1 == res


def limit_rate(max_token=LIMIT_MAX_TOKEN, token_rate=LIMIT_TOKEN_RATE):
    """
    API 接口的速率限制，利用令牌桶实现
    :param max_token: 令牌桶内的最大token
    :param token_rate: 每秒添加的token
    :return:
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            keys = [REDIS_KEY_PREFIX + request.remote_addr]
            res = is_limit(keys, max_token, token_rate)
            if not res:
                abort(429, description="API rate limit exceeded.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
