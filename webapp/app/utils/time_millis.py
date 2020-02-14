import time


def current_time_millis():
    """
    获取毫秒级的时间戳
    """
    return int(round(time.time() * 1000))
