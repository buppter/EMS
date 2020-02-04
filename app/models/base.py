from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, TIMESTAMP, text
from werkzeug.exceptions import abort


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception:
            db.session.rollback()
            abort(500)


class Query(BaseQuery):

    def first_or_400(self, description=None):
        rv = self.first()
        if not rv:
            abort(400, description=description)
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True

    create_time = Column(TIMESTAMP, nullable=False,
                         server_default=text('CURRENT_TIMESTAMP'))
    update_time = Column(TIMESTAMP, nullable=False,
                         server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
