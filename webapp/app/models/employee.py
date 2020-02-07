from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base
from app.models.organization import Node


class Employee(Base):
    __tablename__ = "db_employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False, comment="人员姓名")
    _gender = Column(Integer, default=2, comment="性别")
    org_id = Column(Integer, ForeignKey(Node.id), comment="部门ID")
    org = relationship("Node", back_populates="employee")

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
        return "Employee(id=%r, name=%r, gender=%r, org_id=%r)" % (
            self.id, self.name, self.gender, self.org_id
        )

    def dumps(self):
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["gender"] = self.gender
        data["org"] = self.org.name
        return data
