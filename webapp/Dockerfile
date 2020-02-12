FROM python:3.6

MAINTAINER BUPPTER shixintian@aliyun.com

ADD ./requirements.txt /opt/www/webapp/requirements.txt

WORKDIR /opt/www/webapp

EXPOSE 8000

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
