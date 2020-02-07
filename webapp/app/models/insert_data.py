import random
from faker import Faker

from app.models import db
from app.models.employee import Employee
from app.models.organization import Node


def insert_org_data():
    Node1 = Node(name="伏羲实验室")
    Node2 = Node(name="用户画像组", ancestor=Node1)
    Node3 = Node(name="图像组", ancestor=Node1)
    Node4 = Node(name="平台架构组", ancestor=Node1)
    Node5 = Node(name="强化学习组", ancestor=Node1)
    Node6 = Node(name="虚拟人组", ancestor=Node1)
    Node7 = Node(name="数据组", ancestor=Node4)
    Node8 = Node(name="web开发组", ancestor=Node4)
    Node9 = Node(name="丹炉组", ancestor=Node4)

    data = [Node1, Node2, Node3, Node4, Node5, Node6, Node7, Node8, Node9]
    with db.auto_commit():
        db.session.add_all(data)


def insert_employee_data(times=20):
    for _ in range(times):
        name, gender = random_gender_name()
        org_id = random.choice([7, 8, 9])
        emp = Employee(name=name, gender=gender, org_id=org_id)
        try:
            with db.auto_commit():
                db.session.add(emp)
        except Exception:
            continue


def random_gender_name():
    f = Faker(locale="zh_CN")
    g = random.choice([0, 1])
    if g == 0:
        name = f.name_female()
        gender = "女"
    else:
        name = f.name_male()
        gender = "男"
    return name, gender
