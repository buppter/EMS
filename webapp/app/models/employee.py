from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base
from app.models.department import Department
from app.utils.gender import gender_to_num, num_to_gender


class Employee(Base):
    __tablename__ = "ems_employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, comment="人员姓名")
    _gender = Column(Integer, default=2, comment="性别")
    department_id = Column(Integer, ForeignKey(Department.id), comment="部门ID")
    department = relationship("Department", back_populates="employee")

    @property
    def gender(self):
        return num_to_gender(self._gender)

    @gender.setter
    def gender(self, value):
        data = gender_to_num(value)
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
        data["department"] = self.department.name
        return data
