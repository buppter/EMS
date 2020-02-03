from conf.secure import PER_PAGE_NUM


def simple_select(table_class, **kwargs):
    if kwargs:
        if not set(kwargs.keys()).issubset(
                ('filter', 'first', 'page', 'per_page', 'order_by', 'limit', 'offset')):
            raise Exception("传入的查询关键字错误")
    fields = kwargs.get("filter", None)
    offset = kwargs.get("offset", 0)
    limit = kwargs.get("limit", 0)
    order_by = kwargs.get("order_by", None)
    page = kwargs.get("page", 0)
    per_page = kwargs.get("per_page", 0)
    query_first = kwargs.get("first", False)
    if fields is None:
        session = table_class.query
    else:
        session = table_class.query.filter(*fields)

    if offset:
        session = session.offset(int(offset))
    if limit:
        session = session.limit(int(limit))
    if order_by is not None:
        session = session.order_by(order_by)
    if page and per_page:
        return session.paginate(int(page), int(per_page), False)
    elif page and not per_page:
        return session.paginate(int(page), PER_PAGE_NUM, False)
    if query_first:
        return session.first_or_404()
    return session.all()
