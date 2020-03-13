from sqlalchemy import Column, Integer, String

from .base import Base


class Department(Base):
    __tablename__ = "ems_department"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False, comment="组名称")
    parent_id = Column(Integer, comment="上级部门ID")

    def __init__(self, name, parent_id=None):
        self.name = name
        self.parent_id = parent_id

    def __repr__(self):
        return "Department(name=%r, id=%r, parent_id=%r)" % (
            self.name,
            self.id,
            self.parent_id,
        )

    @staticmethod
    def get_root() -> list:
        """
        返回根节点
        todo:存在多个parent_id为空的情况如何判断
        """
        root = Department.query.filter_by(parent_id=None).exists_or_404(description="部门数据不存在")
        return root

    def dumps_detail(self) -> dict:
        """
        格式化单个部门信息,包含 parent 和 subs 字段
        :return: dict
        """
        department_detail = dict()
        department_detail["id"] = self.id
        department_detail["name"] = self.name
        parent_info = Department.get_node_info(self.parent_id)
        department_detail["parent"] = {"id": self.parent_id, "name": parent_info.name} if parent_info else {}
        sub_nodes_list = self.get_subs()
        department_detail["subs"] = [node.dumps() for node in sub_nodes_list] if sub_nodes_list else []
        return department_detail

    def dumps(self):
        """
        格式化单个部门信息，只包括 id 和 name
        :return:
        """
        department = dict()
        department["id"] = self.id
        department["name"] = self.name
        return department

    def get_subs(self):
        sub_nodes_list = Department.query.filter_by(parent_id=self.id).all()
        return sub_nodes_list

    def dumps_all(self) -> dict:
        """
        格式化所有部门信息
        :return: dict
        """
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        sub_nodes_list = self.get_subs()
        data["subs"] = [node.dumps_all() for node in sub_nodes_list] if sub_nodes_list else []

        return data

    @classmethod
    def get_node_info(cls, node_id=None, node_name=None):
        """
        根据部门id或部门名称获取部门信息
        :param node_id: 部门ID
        :param node_name: 部门名称
        :return:
        """
        if node_id:
            return Department.query.filter_by(id=node_id).first()
        else:
            return Department.query.filter_by(name=node_name).first()
