from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String

from app.models.base import Base
from app.models.organization import Node


class Employee(Base):
    __tablename__ = "db_employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False, comment="人员姓名")
    gender = Column(Integer, default=2, comment="性别")

    @property
    def _gender(self):
        gender_dic = {0: "女", 1: "男", 2: "未知"}
        return gender_dic.get(self.gender)

    @_gender.setter
    def _gender(self, value):
        gender_dic = {"男": 1, "女": 0}
        data = gender_dic.get(value, 2)
        self.gender = data
