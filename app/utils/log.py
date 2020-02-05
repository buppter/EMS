import logging
import logging.handlers

import time
import os


# 增加日志级别过滤
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING


def logger_init(app_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    log_dir = app_dir + "/log/"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    # 日志按每天切分到不同的文件夹下，先检查创建文件夹
    # 注意脚本一次执行时间过短时，是不会触发日志切割的，因此主动拆分
    today = time.strftime("%Y%m%d", time.localtime())
    log_path = log_dir+ today
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    info_handler = logging.handlers.TimedRotatingFileHandler(log_path + "/info.log", "H", 1, 720)
    error_handler = logging.handlers.TimedRotatingFileHandler(log_path + "/error.log", "H", 1, 720)
    warning_handler = logging.handlers.TimedRotatingFileHandler(log_path + "/warning.log", "H", 1, 720)

    info_handler.suffix = "%Y%m%d%H"
    warning_handler.suffix = "%Y%m%d%H"
    error_handler.suffix = "%Y%m%d%H"

    info_filter = InfoFilter()
    error_filter = ErrorFilter()
    warning_filter = WarningFilter()

    info_handler.addFilter(info_filter)
    error_handler.addFilter(error_filter)
    warning_handler.addFilter(warning_filter)

    # 设置formatter
    fmt = '%(asctime)s - %(pathname)s:%(lineno)s - %(message)s'
    formatter = logging.Formatter(fmt)  # 实例化formatter
    info_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(warning_handler)

    logger2 = logging.getLogger("sqlalchemy")
    logger2.setLevel(logging.ERROR)

    sql_handler = logging.handlers.TimedRotatingFileHandler(log_path + "/sqlalchemy_error.log", "H", 1, 720)

    logger2.addHandler(sql_handler)
