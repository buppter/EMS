import random
from faker import Faker

from app.models import db
from app.models.employee import Employee
from app.models.department import Department


def insert_department_data():
    Department1 = Department(name="伏羲实验室")
    Department2 = Department(name="用户画像组", parent=Department1)
    Department3 = Department(name="图像组", parent=Department1)
    Department4 = Department(name="平台架构组", parent=Department1)
    Department5 = Department(name="强化学习组", parent=Department1)
    Department6 = Department(name="虚拟人组", parent=Department1)
    Department7 = Department(name="数据组", parent=Department4)
    Department8 = Department(name="web开发组", parent=Department4)
    Department9 = Department(name="丹炉组", parent=Department4)

    data = [Department1, Department2, Department3, Department4, Department5, Department6, Department7, Department8,
            Department9]
    with db.auto_commit():
        db.session.add_all(data)


def insert_employee_data(times=20):
    for _ in range(times):
        name, gender = random_gender_name()
        department_id = random.choice([7, 8, 9])
        emp = Employee(name=name, gender=gender, department_id=department_id)
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
