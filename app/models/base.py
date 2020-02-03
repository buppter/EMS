from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import Column, TIMESTAMP, text
from werkzeug.exceptions import abort


class Query(BaseQuery):

    def first_or_400(self):
        rv = self.first()
        if not rv:
            abort(400)
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True

    create_time = Column(TIMESTAMP, nullable=False,
                         server_default=text('CURRENT_TIMESTAMP'))
    update_time = Column(TIMESTAMP, nullable=False,
                         server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
