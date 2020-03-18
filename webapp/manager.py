from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

from app.utils.script import Insert, Create, Drop

"""
可选运行环境：
"development": Development,
"test": Testing,
"production": Production,
"""
app = create_app("production")

manager = Manager(app)

manager.add_command("db", MigrateCommand)
# 插入一些Fake数据
manager.add_command("insert", Insert())
# 创建数据库表
manager.add_command("create", Create())
# 删除数据库表
manager.add_command("drop", Drop())

if __name__ == "__main__":
    manager.run()
