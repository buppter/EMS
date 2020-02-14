import redis

from flask import current_app

from conf.config import REDIS_KEY_PREFIX


class Redis:
    """
    Redis 客户端以及封装相关的 Redis 命令
    """

    @staticmethod
    def _get_r():
        REDIS_CONF = current_app.config["REDIS_URL"]
        pool = redis.ConnectionPool(host=REDIS_CONF["HOST"],
                                    port=REDIS_CONF["PORT"],
                                    password=REDIS_CONF.get("PASSWORD", None),
                                    decode_responses=True)

        redis_cli = redis.StrictRedis(connection_pool=pool)
        return redis_cli

    @classmethod
    def delete(cls, key):
        r = cls._get_r()
        return r.delete(REDIS_KEY_PREFIX + key)

    @classmethod
    def script(cls, lua):
        r = cls._get_r()
        script = r.register_script(lua)
        return script
