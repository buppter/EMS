import sys
import unittest

from flask import current_app

sys.path.append("../")
from tests.base import BaseTest
from app.models import db
from app.api.v1 import department_bp


class DepartmentTestCase(BaseTest):

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_retrieve_department_is_not_found(self):
        res = self.client.get("/v1/departments/1000")
        self.assertEqual(res.status_code, 404)
        res = res.json
        self.assertEqual(res["code"], 404)
        self.assertEqual(res["data"], [])
        self.clean_redis_data()

    def test_retrieve_single_department(self):
        res = self.client.get("v1/departments/1")
        self.assertEqual(res.status_code, 200)
        res = res.json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], dict)
        self.assertTrue("name" in res["data"])
        self.clean_redis_data()

    def test_retrieve_all_departments(self):
        res = self.client.get("/v1/departments")
        self.assertEqual(res.status_code, 200)
        res = res.json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], list)
        self.assertTrue("subs" in res["data"][0])
        self.clean_redis_data()

    def test_create_no_data(self):
        res = self.client.post("/v1/departments", json={})
        self.assertEqual(res.status_code, 415)
        res = res.json
        self.assertEqual(res["code"], 415)
        self.assertTrue("json" in res["msg"])
        self.clean_redis_data()

    def test_create_bad_data(self):
        res = self.client.post("/v1/departments", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("不完整" in res["msg"])
        self.clean_redis_data()

    def test_create_not_exist_parent(self):
        res = self.client.post("/v1/departments", json={"name": "test", "parent": "test"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("不存在" in res['msg'])
        self.clean_redis_data()

    def test_create_exist_department(self):
        res = self.client.post("v1/departments", json={"name": "web开发组", "parent": "平台架构组"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("已存在" in res["msg"])
        self.clean_redis_data()

    def test_create_right_data(self):
        res = self.client.post("/v1/departments", json={"name": "前端开发组", "parent": "平台架构组"})
        self.assertEqual(res.status_code, 201)
        res = res.json
        self.assertEqual(res["code"], 201)
        self.assertTrue("created" in res["msg"])
        self.clean_redis_data()

    def test_update_no_data(self):
        res = self.client.put("/v1/departments/2", json={})
        self.assertEqual(res.status_code, 415)
        self.assertEqual(res.json["code"], 415)
        self.assertTrue("json" in res.json["msg"])
        self.clean_redis_data()

    def test_update_no_exist_parent(self):
        res = self.client.put("/v1/departments/2", json={"name": "test", "parent": "test22"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['code'], 400)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_update_not_complete_data(self):
        res = self.client.put("/v1/departments/2", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['code'], 400)
        self.assertTrue("不完整" in res.json["msg"])
        self.clean_redis_data()

    def test_update_right_data(self):
        res = self.client.put("/v1/departments/2", json={"name": "test2", "parent": "web开发组"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])
        self.clean_redis_data()

    def test_update_exist_name_not_self(self):
        res = self.client.put("/v1/departments/4", json={"name": "web开发组", "parent": "伏羲实验室"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("已存在" in res["msg"])
        self.clean_redis_data()

    def test_update_exist_name_is_self(self):
        res = self.client.put("/v1/departments/8", json={"name": "web开发组", "parent": "强化学习组"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])
        self.clean_redis_data()

    def test_delete_wrong_id(self):
        res = self.client.delete("/v1/departments/100")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_delete_right_id(self):
        res = self.client.delete("/v1/departments/3")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])
        self.clean_redis_data()

    def test_get_exist_department_parent(self):
        res = self.client.get("/v1/departments/3/parent")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("id" in res.json["data"])
        self.clean_redis_data()

    def test_get_not_exist_department_parent(self):
        res = self.client.get("/v1/departments/100/parent")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.clean_redis_data()

    def test_get_exist_department_sub(self):
        res = self.client.get("/v1/departments/1/subs")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_not_exist_department_sub(self):
        res = self.client.get("/v1/departments/100/subs")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.clean_redis_data()

    def test_get_exist_department_sub_with_queries(self):
        res = self.client.get("/v1/departments/1/subs?page=1&per_page=1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_department_sub_with_queries_2(self):
        res = self.client.get("/v1/departments/1/subs?page=1&per_page=fdd")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_department_sub_with_queries_3(self):
        res = self.client.get("/v1/departments/3/subs?limit=1&offset=3")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_department_siblings_without_query(self):
        res = self.client.get("v1/departments/4/siblings")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_department_siblings_without_queries_1(self):
        res = self.client.get("v1/departments/4/siblings?page=1&per_page=5")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_department_siblings_without_queries_2(self):
        res = self.client.get("v1/departments/4/siblings?offset=2&limit=2")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_query_with_error(self):
        from app.utils.query import select
        from app.models.department import Department
        try:
            select(Department, error=111)
        except Exception as e:
            self.assertTrue("错误" in e.args[0])

    def test_query_first_or_404(self):
        from app.utils.query import select
        from app.models.department import Department
        try:
            select(Department, filter={"id": 100}, first=True)
        except Exception as e:
            self.assertEqual(e.code, 404)

    def test_db_rollback(self):
        from app.models.department import Department
        try:
            with db.auto_commit():
                db.session.add(Department(name="伏羲实验室"))
        except Exception as e:
            self.assertEqual(e.code, 500)

    @staticmethod
    @department_bp.route("/test_500")
    def server_error():
        from app.models.department import Department

        with db.auto_commit():
            db.session.add(Department(name="伏羲实验室"))

    def test_500(self):
        res = self.client.get("/v1/test_500")
        self.assertEqual(res.status_code, 500)
        self.assertEqual(res.json["code"], 500)

    def test_405(self):
        res = self.client.post("/v1/departments/1", json={})
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.json["code"], 405)
        self.clean_redis_data()

    def test_limit_rate(self):
        for _ in range(15):
            res = self.client.get("/v1/departments")
        self.assertEqual(res.status_code, 429)
        self.assertEqual(res.json["code"], 429)
        self.assertTrue("limit" in res.json["msg"])
        self.clean_redis_data()


if __name__ == '__main__':
    unittest.main()
