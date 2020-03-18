from sqlalchemy import Column, Integer, String, SmallInteger

from app.models import Department
from app.models.base import Base


class Employee(Base):
    __tablename__ = "ems_employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, comment="人员姓名")
    _gender = Column(SmallInteger, default=2, comment="性别")
    department_id = Column(Integer, comment="部门ID")

    @property
    def gender(self):
        gender_dic = {0: "女", 1: "男", 2: "未知"}
        return gender_dic.get(self._gender)

    @gender.setter
    def gender(self, value):
        gender_dic = {"男": 1, "女": 0}
        data = gender_dic.get(value, 2)
        self._gender = data

    def dumps(self):
        """
        格式化单个员工信息
        :return: dict
        """
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["gender"] = self.gender
        department_node = Department.query.filter_by(id=self.department_id).first()
        data["department"] = department_node.name if department_node else []
        return data
