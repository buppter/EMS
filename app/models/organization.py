from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.collections import attribute_mapped_collection

from .base import Base


class Node(Base):
    __tablename__ = "db_node"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False, comment="组名称")
    ancestor_id = Column(Integer, ForeignKey(id))

    descendant = relationship("Node", cascade="all, delete-orphan", backref=backref("ancestor", remote_side=id),
                              collection_class=attribute_mapped_collection("name"))

    def __init__(self, name, ancestor=None):
        self.name = name
        self.ancestor = ancestor

    def __repr__(self):
        return "Node(name=%r, id=%r, ancestor_id=%r)" % (
            self.name,
            self.id,
            self.ancestor_id,
        )

    @staticmethod
    def get_root():
        """
        返回根节点
        todo:存在多个ancestor_id为空的情况如何判断
        """
        root = Node.query.filter(Node.ancestor_id == None).first_or_404()
        return root

    def to_dict(self):
        org = dict()
        org["id"] = self.id
        org["name"] = self.name
        return org

    def dumps(self):
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["descendant"] = [c.dumps() for c in self.descendant.values()] if self.descendant else []

        return [data]
