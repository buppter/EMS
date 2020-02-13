from flask_script import Command, Option


class Insert(Command):
    """
    insert data to database
    """

    def __init__(self, default_times=20):
        self.default_times = default_times

    def get_options(self):
        return [
            Option('-t', '--times', dest="times", default=self.default_times),
        ]

    def run(self, times):
        from app.models.insert_data import insert_employee_data, insert_department_data
        try:
            times = int(times)
        except ValueError:
            times = self.default_times
        insert_department_data()
        insert_employee_data(times)


class Create(Command):
    """create all tables"""

    def run(self):
        from app.models import db
        from app.models.department import Department
        from app.models.employee import Employee
        db.drop_all()
        db.create_all()


class Drop(Command):
    """drop all tables"""

    def run(self):
        from app.models import db
        db.drop_all()
