from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.collections import attribute_mapped_collection

from .base import Base


class Department(Base):
    __tablename__ = "ems_department"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False, comment="组名称")
    parent_id = Column(Integer, ForeignKey(id), comment="上级部门ID")

    subordinate = relationship("Department", cascade="all, delete-orphan", backref=backref("parent", remote_side=id),
                               collection_class=attribute_mapped_collection("name"))

    employee = relationship("Employee", back_populates="department", lazy="dynamic")

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return "Department(name=%r, id=%r, parent_id=%r)" % (
            self.name,
            self.id,
            self.parent_id,
        )

    @staticmethod
    def get_root():
        """
        返回根节点
        todo:存在多个parent_id为空的情况如何判断
        """
        root = Department.query.filter(Department.parent_id == None).first_or_404(description="部门数据不存在")
        return root

    def dumps(self):
        """
        格式化单个部门信息
        :return: dict
        """
        department = dict()
        department["id"] = self.id
        department["name"] = self.name
        return department

    def dumps_all(self):
        """
        格式化所有部门信息
        :return: dict
        """
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["subs"] = [c.dumps_all() for c in self.subordinate.values()] if self.subordinate else []

        return [data]
