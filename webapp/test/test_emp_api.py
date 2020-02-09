import sys
import unittest

sys.path.append("../")

from test.base import BaseTest


class EmpTestCase(BaseTest):

    def test_get_all_emp_without_queries(self):
        res = self.client.get("/v1/employees")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_get_all_emp_with_page_query(self):
        res = self.client.get("/v1/employees?page=1&per_page=10")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertEqual(len(res.json["data"]), 10)
        self.clean_redis_data()

    def test_all_get_emp_with_limit_offset_query(self):
        res = self.client.get("/v1/employees?offset=10&limit=5")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertEqual(len(res.json["data"]), 5)
        self.clean_redis_data()

    def test_all_get_emp_with_name_query_200(self):
        self.client.post("/v1/employees", json={"name": "test", "gender": "男", "org": "图像组"})
        res = self.client.get("/v1/employees?name=test")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_all_get_emp_with_name_query_404(self):
        res = self.client.get("/v1/employees?name=testnot")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.clean_redis_data()

    def test_all_get_emp_with_gender_query(self):
        res = self.client.get("/v1/employees?gender=男")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_all_get_emp_with_org_query(self):
        res = self.client.get("/v1/employees?org=web开发组")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_create_employee_with_error_json_data(self):
        res = self.client.post("/v1/employees", json={})
        self.assertEqual(res.status_code, 415)
        self.assertEqual(res.json["code"], 415)
        self.assertTrue("json" in res.json["msg"])
        self.clean_redis_data()

    def test_create_employee_with_not_complete_data(self):
        res = self.client.post("/v1/employees", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["code"], 400)
        self.assertTrue("不完整" in res.json["msg"])
        self.clean_redis_data()

    def test_create_employee_with_not_exist_org(self):
        res = self.client.post("/v1/employees", json={"name": "test", "gender": "男", "org": "not exist"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["code"], 400)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_create_employee_with_right_data(self):
        res = self.client.post("/v1/employees", json={"name": "test", "gender": "男", "org": "图像组"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json["code"], 201)
        self.assertTrue("created" in res.json["msg"])
        self.clean_redis_data()

    def test_get_single_emp_with_200(self):
        res = self.client.get("/v1/employees/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_get_single_emp_with_404(self):
        res = self.client.get("/v1/employees/500")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_update_emp_with_200(self):
        res = self.client.put("/v1/employees/1", json={"name": "test11", "gender": "男", "org": "web开发组"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_update_emp_with_415(self):
        res = self.client.put("/v1/employees/1", json={})
        self.assertEqual(res.status_code, 415)
        self.assertEqual(res.json["code"], 415)
        self.clean_redis_data()

    def test_update_emp_with_400_1(self):
        res = self.client.put("/v1/employees/1", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["code"], 400)
        self.assertTrue("不完整" in res.json["msg"])
        self.clean_redis_data()

    def test_update_emp_with_400_2(self):
        res = self.client.put("/v1/employees/1", json={"name": "test", "gender": "男", "org": "test"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["code"], 400)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_delete_emp_with_200(self):
        res = self.client.delete("/v1/employees/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.clean_redis_data()

    def test_api_405(self):
        res = self.client.post("/v1/employees/2")
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.json["code"], 405)
        self.clean_redis_data()


if __name__ == '__main__':
    unittest.main()
