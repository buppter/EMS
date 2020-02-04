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
        res = self.client.get("/v1/org/1000").json
        self.assertEqual(res["code"], 404)
        self.assertEqual(res["data"], [])

    def test_retrieve_single_node(self):
        res = self.client.get("v1/org/1").json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], dict)
        self.assertTrue("name" in res["data"])

    def test_retrieve_all_nodes(self):
        res = self.client.get("/v1/orgs").json
        self.assertEqual(res["code"], 200)
        self.assertIsInstance(res["data"], list)
        self.assertTrue("descendant" in res["data"][0])

    def test_create_no_data(self):
        res = self.client.post("/v1/orgs", json={}).json
        self.assertEqual(res["code"], 400)

    def test_create_bad_data(self):
        res = self.client.post("/v1/orgs", json={"name": "test"}).json
        self.assertEqual(res["code"], 400)

    def test_create_not_exist_ancestor(self):
        res = self.client.post("/v1/orgs", json={"name": "test", "ancestor": "test"}).json
        self.assertEqual(res["code"], 400)

    def test_create_right_data(self):
        res = self.client.post("/v1/orgs", json={"name": "test", "ancestor": "平台开发组"}).json
        self.assertEqual(res["code"], 201)
        self.assertEqual(res["data"], [])


if __name__ == '__main__':
    unittest.main()
