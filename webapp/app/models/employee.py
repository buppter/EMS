from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base
from app.models.department import Department


class Employee(Base):
    __tablename__ = "ems_employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, comment="人员姓名")
    _gender = Column(Integer, default=2, comment="性别")
    department_id = Column(Integer, ForeignKey(Department.id), comment="部门ID")
    department = relationship("Department", back_populates="employee")

    @property
    def gender(self):
        gender_dic = {0: "女", 1: "男", 2: "未知"}
        return gender_dic.get(self._gender)

    @gender.setter
    def gender(self, value):
        gender_dic = {"男": 1, "女": 0}
        data = gender_dic.get(value, 2)
        self._gender = data

    def __repr__(self):
        return "Employee(id=%r, name=%r, gender=%r, department_id=%r)" % (
            self.id, self.name, self.gender, self.department_id
        )

    def dumps(self):
        """
        格式化单个员工信息
        :return: dict
        """
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["gender"] = self.gender
        data["department"] = self.department.name
        return data
