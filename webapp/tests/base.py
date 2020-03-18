import unittest
import sys

sys.path.append("../")

from app import create_app
from app.models import db
from app.utils.insert_data import insert_department_data, insert_employee_data


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()
        insert_department_data()
        insert_employee_data()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @staticmethod
    def clean_redis_data():
        from app.utils.redis_cli import Redis
        Redis.delete("127.0.0.1")