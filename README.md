# EMS
[![Build Status](https://www.travis-ci.org/buppter/EMS.svg?branch=master)](https://www.travis-ci.org/buppter/EMS)
[![codecov](https://codecov.io/gh/buppter/EMS/branch/master/graph/badge.svg)](https://codecov.io/gh/buppter/EMS)
![Python](https://img.shields.io/badge/Python-3.6-orange.svg)
[![MIT License][license-shield]][license-url]

员工管理系统(Employee Management System, EMS)，基于 Python 的 Flask 框架构建的RESTful Web 应用。提供了 API 接口来管理员工和部门组织，功能主要包括对员工和部门的增删改查。

## 目录结构

```
FileTree
├── LICENSE
├── README.md
├── db                    # 数据库相关配置
├── docker-compose.yml    # docker-compose 配置
├── nginx                 # nginx 配置文件
└── webapp                # Flask 项目主要代码
    ├── Dockerfile        # Flask 项目 Dockerfile 
    ├── __init__.py
    ├── app               # 包括 routes，models，utils 相关代码
    ├── conf              # 项目配置
    ├── manager.py        # 项目入口
    ├── migrations        # 数据库迁移
    ├── requirements.txt  # 项目依赖
    ├── tests             # 单元测试
    └── uwsgi.ini         # uwsgi 配置
    └── wait-for-it.sh    # wait-for 脚本，主要用来等待数据库启动

```

## 特性

### 1. 接口支持分页，过滤，偏移

尽可能地符合 RESTful 规范，接口支持 query 参数：`page`, `per_page`, `limit`, `offset`, 以及其他具体的过滤参数。详见 [接口文档](https://github.com/buppter/EMS/blob/master/webapp/README.md)

### 2. 接口速率限制

利用 `Redis` 以及 `Lua` 根据令牌桶算法来实现接口限速，使得限速更加平滑且优雅

### 3. 可使用 Docker 部署

提供 `Docker` 部署方案，并利用 `docker-compose` 编排 `MySQL`，`Redis`，`Nginx`，部署运行更加简便快捷

## 下载安装

该项目运行方式灵活，可以在 Docker 或本地环境中运行

### 1. Docker 中运行

*请先安装好 Docker 和 docker-compose*

#### 安装步骤

- 克隆本仓库

  ```bash
  git clone https://github.com/buppter/EMS.git
  ```

- 运行程序

  ```shell
  docker-compose up --build
  ```

- 访问 `127.0.0.1/v1/departments` 查看返回的数据

### 2. 本地环境运行

*请先在本地环境中安装好 `MySQL`，`Redis`，`Nginx(可选)`，并创建所需数据库*

#### 安装步骤

- 克隆本仓库

  ```bash
  git clone https://github.com/buppter/EMS.git
  ```

- 安装依赖

  ```bash
  cd webapp
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
  ```

- 修改配置信息

   修改 `webapp/conf ` 下的 `secure.py` 文件中的数据库配置信息

  *数据库配置信息根据运行环境不同，有 `Development`，`Testing`，`Production` 三种环境，请根据需求修改不同的配置信息*

- 启动程序

  项目入口文件为 `webapp/manager.py` ，在文件中配置的为 `Production` 环境；如需修改运行环境，请在 `app = create_app("production")` 这一行中进行更换。

  **1. 通过 `uwsgi` 启动运行**

  ```bash
  cd webapp
  uwsgi --ini uwsgi.ini
  ```

  通过访问 `127.0.0.1:8000/v1/departments` 查看返回数据（**在访问前需先插入数据**）

  **2. 通过 `Werkzeug` 启动运行**

  ```bash
  cd webapp
  python3 manager.py runserver
  ```

  通过访问 `127.0.0.1:5000/v1/departments` 查看返回数据（**在访问前需先插入数据**）

- 导入Fake数据（可选）

  项目提供 Fake 数据的导入

  ```bash
  # 生成表
  python3 manager.py create
  
  # 插入 Fake 数据
  # 参数 -t 指所插入的 employee 数据量
  python3 manager.py insert -t 100
  ```

- 配置Nginx（可选）

  在 `nginx` 文件夹下提供了项目 conf 文件 `ems.conf`，拷贝到本地 nginx 的配置文件夹，运行 `nginx -s reload` 是配置文件生效。

  之后访问 `127.0.0.1/v1/employees` 查看返回数据，域名可在 `ems.conf` 中进行修改。

### 3. 其余配置

*其余配置参数都位于 `webapp/conf/config.py` 中*

#### （1） 接口限速

修改配置文件中的 `LIMIT_MAX_TOKEN` 和 `LIMIT_TOKEN_RATE` 参数，默认为 `10` 。

`LIMIT_MAX_TOKEN` 指令牌桶中最大的 TOKEN 数量，`LIMIT_TOKEN_RATE` 指每秒向令牌桶中添加 TOKEN 的速率，根据需求自行修改。

#### （2）PER_PAGE

当URL中传入 `page` 参数而缺省 `per_page` 参数时，默认每页显示 `20` 条数据。

#### （3）Redis 的 Key 前缀

修改配置文件中 `REDIS_KEY_PREFIX` 参数即可。

## 接口列表

具体的接口列表，请查看 [接口文档](https://github.com/buppter/EMS/blob/master/webapp/README.md)

## License

[MIT][license-url]



[license-shield]: https://img.shields.io/github/license/buppter/EMS.svg
[license-url]: https://github.com/buppter/EMS/blob/master/LICENSE

