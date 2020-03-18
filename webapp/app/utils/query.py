from conf.config import PER_PAGE_NUM


def select(table_class, **kwargs):
    """
    封装了查询接口，主要是方便query参数的使用
    :param table_class: 所查询的数据库类
    :param kwargs: 其他query参数
    :return:
    """
    if kwargs:
        if not set(kwargs.keys()).issubset(
                ('filter', 'first', 'page', 'per_page', 'order_by', 'limit', 'offset', 'exists')):
            raise Exception("传入的查询关键字错误")
    fields = kwargs.pop("filter", None)
    offset = kwargs.pop("offset", 0)
    offset = to_digit(offset)
    limit = kwargs.pop("limit", 0)
    limit = to_digit(limit)
    page = kwargs.pop("page", 0)
    page = to_digit(page)
    per_page = kwargs.pop("per_page", 0)
    per_page = to_digit(per_page)
    query_first = kwargs.pop("first", False)
    exists = kwargs.pop("exists", False)

    if isinstance(fields, dict) and fields:
        session = table_class.query.filter_by(**fields)
    elif isinstance(fields, list):
        session = table_class.query.filter(*fields)
    else:
        session = table_class.query

    if exists:
        session.exists_or_404(description="not found")

    if offset:
        session = session.offset(offset)

    if limit:
        session = session.limit(limit)

    if page and per_page:
        return session.paginate(page, per_page, False).items
    elif page and not per_page:
        return session.paginate(page, PER_PAGE_NUM, False).items
    if query_first:
        return session.first_or_404(description="not found")
    return session.all()


def to_digit(data):
    try:
        data = int(data)
    except ValueError:
        data = 0
    return data
