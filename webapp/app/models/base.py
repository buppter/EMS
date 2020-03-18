import logging
import traceback
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, TIMESTAMP, text, SmallInteger
from werkzeug.exceptions import abort


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception:
            db.session.rollback()
            logging.error('insert data into mysql error: %s' % traceback.format_exc())
            abort(500)


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def first_or_400(self, description=None):
        rv = self.first()
        if not rv:
            abort(400, description=description)
        return rv

    def exists_or_404(self, description=None):
        rv = self.all()
        if not rv:
            abort(404, description=description)
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True

    create_time = Column(TIMESTAMP, nullable=False,
                         server_default=text('CURRENT_TIMESTAMP'))
    update_time = Column(TIMESTAMP, nullable=False,
                         server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    status = Column(SmallInteger, default=1)

    def delete(self):
        self.status = 0
