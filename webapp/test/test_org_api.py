import sys
import unittest

from flask import current_app

sys.path.append("../")

from webapp.test.base import BaseTest
from app.models import db
from app.api.v1 import org_bp



class OrgTestCase(BaseTest):

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_retrieve_node_is_not_found(self):
        res = self.client.get("/v1/orgs/1000")
        self.assertEqual(res.status_code, 404)
        res = res.json
        self.assertEqual(res["code"], 404)
        self.assertEqual(res["data"], [])
        self.clean_redis_data()

    def test_retrieve_single_node(self):
        res = self.client.get("v1/orgs/1")
        self.assertEqual(res.status_code, 200)
        res = res.json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], dict)
        self.assertTrue("name" in res["data"])
        self.clean_redis_data()

    def test_retrieve_all_nodes(self):
        res = self.client.get("/v1/orgs")
        self.assertEqual(res.status_code, 200)
        res = res.json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], list)
        self.assertTrue("subs" in res["data"][0])
        self.clean_redis_data()

    def test_create_no_data(self):
        res = self.client.post("/v1/orgs", json={})
        self.assertEqual(res.status_code, 415)
        res = res.json
        self.assertEqual(res["code"], 415)
        self.assertTrue("json" in res["msg"])
        self.clean_redis_data()

    def test_create_bad_data(self):
        res = self.client.post("/v1/orgs", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("不完整" in res["msg"])
        self.clean_redis_data()

    def test_create_not_exist_ancestor(self):
        res = self.client.post("/v1/orgs", json={"name": "test", "ancestor": "test"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("不存在" in res['msg'])
        self.clean_redis_data()

    def test_create_exist_org(self):
        res = self.client.post("v1/orgs", json={"name": "web开发组", "ancestor": "平台架构组"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("已存在" in res["msg"])
        self.clean_redis_data()

    def test_create_right_data(self):
        res = self.client.post("/v1/orgs", json={"name": "前端开发组", "ancestor": "平台架构组"})
        self.assertEqual(res.status_code, 201)
        res = res.json
        self.assertEqual(res["code"], 201)
        self.assertEqual(res["data"], [])
        self.assertTrue("created" in res["msg"])
        self.clean_redis_data()

    def test_update_no_data(self):
        res = self.client.put("/v1/orgs/2", json={})
        self.assertEqual(res.status_code, 415)
        self.assertEqual(res.json["code"], 415)
        self.assertTrue("json" in res.json["msg"])
        self.clean_redis_data()

    def test_update_no_exist_ancestor(self):
        res = self.client.put("/v1/orgs/2", json={"name": "test", "ancestor": "test22"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['code'], 400)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_update_not_complete_data(self):
        res = self.client.put("/v1/orgs/2", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['code'], 400)
        self.assertTrue("不完整" in res.json["msg"])
        self.clean_redis_data()

    def test_update_right_data(self):
        res = self.client.put("/v1/orgs/2", json={"name": "test2", "ancestor": "web开发组"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])
        self.clean_redis_data()

    def test_delete_wrong_id(self):
        res = self.client.delete("/v1/orgs/100")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.assertTrue("不存在" in res.json["msg"])
        self.clean_redis_data()

    def test_delete_right_id(self):
        res = self.client.delete("/v1/orgs/3")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])
        self.clean_redis_data()

    def test_get_exist_node_ancestor(self):
        res = self.client.get("/v1/orgs/ancestor/3")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("id" in res.json["data"])
        self.clean_redis_data()

    def test_get_not_exist_node_ancestor(self):
        res = self.client.get("/v1/orgs/ancestor/100")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.clean_redis_data()

    def test_get_exist_node_sub(self):
        res = self.client.get("/v1/orgs/subs/1")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_not_exist_node_sub(self):
        res = self.client.get("/v1/orgs/subs/100")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.clean_redis_data()

    def test_get_exist_node_sub_with_queries(self):
        res = self.client.get("/v1/orgs/subs/1?page=1&per_page=1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_node_sub_with_queries_2(self):
        res = self.client.get("/v1/orgs/subs/1?page=1&per_page=fdd")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_get_exist_node_sub_with_queries_3(self):
        res = self.client.get("/v1/orgs/subs/3?limit=1&offset=3")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertIsInstance(res.json["data"], list)
        self.clean_redis_data()

    def test_query_with_error(self):
        from app.utils.query import select
        from app.models.organization import Node
        try:
            select(Node, error=111)
        except Exception as e:
            self.assertTrue("错误" in e.args[0])

    def test_query_first_or_404(self):
        from app.utils.query import select
        from app.models.organization import Node
        try:
            select(Node, filter=[Node.id == 100], first=True)
        except Exception as e:
            self.assertEqual(e.code, 404)

    def test_db_rollback(self):
        from app.models.organization import Node
        try:
            with db.auto_commit():
                db.session.add(Node(name="伏羲实验室"))
        except Exception as e:
            self.assertEqual(e.code, 500)

    @staticmethod
    @org_bp.route("/test_500")
    def server_error():
        from app.models.organization import Node

        with db.auto_commit():
            db.session.add(Node(name="伏羲实验室"))

    def test_500(self):
        res = self.client.get("/v1/test_500")
        self.assertEqual(res.status_code, 500)
        self.assertEqual(res.json["code"], 500)

    def test_405(self):
        res = self.client.post("/v1/orgs/1", json={})
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.json["code"], 405)
        self.clean_redis_data()

    def test_limit_rate(self):
        for _ in range(11):
            res = self.client.get("/v1/orgs")
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json["code"], 403)
        self.assertTrue("limit" in res.json["msg"])
        self.clean_redis_data()


if __name__ == '__main__':
    unittest.main()
