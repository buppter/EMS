import redis

from flask import current_app

from conf.config import REDIS_KEY_PREFIX


class Redis:

    @staticmethod
    def _get_r():
        REDIS_CONF = current_app.config["REDIS_URL"]
        redis_cli = redis.StrictRedis(host=REDIS_CONF["HOST"],
                                      port=REDIS_CONF["PORT"],
                                      password=REDIS_CONF.get("PASSWORD", None),
                                      decode_responses=True)
        return redis_cli

    @classmethod
    def setex(cls, key, time, value):
        r = cls._get_r()
        return r.setex(REDIS_KEY_PREFIX + key, time, value)

    @classmethod
    def get(cls, key):
        r = cls._get_r()
        return r.get(REDIS_KEY_PREFIX + key)

    @classmethod
    def incr(cls, key):
        r = cls._get_r()
        return r.incr(REDIS_KEY_PREFIX + key)
