import unittest
import sys
from flask import current_app

sys.path.append("../")

from app import create_app
from app.models import db
from app.models.organization import Node


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.inset_test_data()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @staticmethod
    def inset_test_data():
        node1 = Node("伏羲实验室")
        node2 = Node("平台开发组", ancestor=node1)
        node3 = Node("web开发组", ancestor=node2)

        db.session.add_all([node1, node2, node3])
        db.session.commit()

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_retrieve_node_is_not_found(self):
        res = self.client.get("/v1/orgs/1000")
        self.assertEqual(res.status_code, 404)
        res = res.json
        self.assertEqual(res["code"], 404)
        self.assertEqual(res["data"], [])

    def test_retrieve_single_node(self):
        res = self.client.get("v1/orgs/1")
        self.assertEqual(res.status_code, 200)
        res = res.json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], dict)
        self.assertTrue("name" in res["data"])

    def test_retrieve_all_nodes(self):
        res = self.client.get("/v1/orgs")
        self.assertEqual(res.status_code, 200)
        res = res.json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], list)
        self.assertTrue("descendant" in res["data"][0])

    def test_create_no_data(self):
        res = self.client.post("/v1/orgs", json={})
        self.assertEqual(res.status_code, 415)
        res = res.json
        self.assertEqual(res["code"], 415)
        self.assertTrue("json" in res["msg"])

    def test_create_bad_data(self):
        res = self.client.post("/v1/orgs", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("不完整" in res["msg"])

    def test_create_not_exist_ancestor(self):
        res = self.client.post("/v1/orgs", json={"name": "test", "ancestor": "test"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("不存在" in res['msg'])

    def test_create_exist_org(self):
        res = self.client.post("v1/orgs", json={"name": "平台开发组", "ancestor": "伏羲实验室"})
        self.assertEqual(res.status_code, 400)
        res = res.json
        self.assertEqual(res["code"], 400)
        self.assertTrue("已存在" in res["msg"])

    def test_create_right_data(self):
        res = self.client.post("/v1/orgs", json={"name": "test", "ancestor": "平台开发组"})
        self.assertEqual(res.status_code, 201)
        res = res.json
        self.assertEqual(res["code"], 201)
        self.assertEqual(res["data"], [])
        self.assertTrue("created" in res["msg"])

    def test_update_no_data(self):
        res = self.client.put("/v1/orgs/2", json={})
        self.assertEqual(res.status_code, 415)
        self.assertEqual(res.json["code"], 415)
        self.assertTrue("json" in res.json["msg"])

    def test_update_no_exist_ancestor(self):
        res = self.client.put("/v1/orgs/2", json={"name": "test", "ancestor": "test22"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['code'], 400)
        self.assertTrue("不存在" in res.json["msg"])

    def test_update_not_complete_data(self):
        res = self.client.put("/v1/orgs/2", json={"name": "test"})
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['code'], 400)
        self.assertTrue("不完整" in res.json["msg"])

    def test_update_right_data(self):
        res = self.client.put("/v1/orgs/2", json={"name": "test2", "ancestor": "web开发组"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])

    def test_delete_wrong_id(self):
        res = self.client.delete("/v1/orgs/100")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["code"], 404)
        self.assertTrue("not found" in res.json["msg"])

    def test_delete_right_id(self):
        res = self.client.delete("/v1/orgs/3")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["code"], 200)
        self.assertTrue("success" in res.json["msg"])


if __name__ == '__main__':
    unittest.main()
