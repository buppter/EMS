from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

from app.utils.script import Insert, Create, Drop

app = create_app()

manager = Manager(app)

manager.add_command("db", MigrateCommand)
manager.add_command("insert", Insert())
manager.add_command("create", Create())
manager.add_command("drop", Drop())

if __name__ == "__main__":
    manager.run()
