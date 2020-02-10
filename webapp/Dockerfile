FROM python:3.6

MAINTAINER BUPPTER shixintian@aliyun.com

ADD . /opt/www/webapp

WORKDIR /opt/www/webapp

EXPOSE 8000

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

CMD python3 manager.py create && python3 manager.py insert -t 200 && uwsgi --ini uwsgi.ini