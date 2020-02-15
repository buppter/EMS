# 接口文档

## Base URL

`127.0.0.1/v1`

## 全局响应码

项目中，接口返回的响应码主要跟 HTTP 状态码一致

| code |        message         |             说明             |
| :--: | :--------------------: | :--------------------------: |
| 200  |        success         |           请求成功           |
| 201  |        created         |        POST 创建成功         |
| 400  |      bad request       |   POST 或 PUT 的数据不完整   |
| 404  |       not found        |       请求的资源不存在       |
| 405  |   method not allowed   |        请求方法不允许        |
| 415  | unsupported media type | POST 或 PUT 的数据类型不正确 |
| 429  |   too many requests    |         请求过于频繁         |
| 500  |      server error      |      服务器或数据库错误      |

## 部门管理接口

### 1. 查看所有部门信息

获取数据库内所有的部门信息

#### URL

 `/departments`

#### 请求方式

`GET`

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":[
        {
            "id":1,
            "name":"伏羲实验室",
            "subs":[
                {
                    "id":4,
                    "name":"平台架构组",
                    "subs":[
                        {
                            "id":7,
                            "name":"数据研发组",
                            "subs":[]
                        }
                    ]
                }
            ]
        }
    ]
}
```

### 2. 创建部门

创建一个新的部门信息

#### URL

`/departments`

#### 请求方式

`POST`

#### 请求参数

请求参数为 `application/json` 格式

| 参数名称 | 是否必须 | 参数类型 |   参数位置   |      参数说明      |
| :------: | :------: | :------: | :----------: | :----------------: |
|   name   |    Y     |  string  | request data |      部门名称      |
|  parent  |    Y     |  string  | request data | 部门的上级部门名称 |

示例：

```json
{"name":"前端开发组", "parent":"平台架构组"}
```

#### 成功响应示例

```json
{
    "code":201,
    "msg":"created",
    "data":{
        "id":11,
        "name":"前端开发组",
        "parent":{
            "id":4,
            "name":"平台架构组"
        },
        "subs":[]
    }
}
```

### 3. 查看单个部门

查看单个部门的具体信息

#### URL

`/departments/{department_id}`

#### 请求方式

`GET`

#### 请求参数

|   参数名称    | 是否必须 | 参数类型 | 参数位置 | 参数说明 |
| :-----------: | :------: | :------: | :------: | :------: |
| department_id |    Y     |   int    | url path |  部门ID  |

示例：

```
/departments/11
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":{
        "id":11,
        "name":"前端开发组",
        "parent":{
            "id":4,
            "name":"平台架构组"
        },
        "subs":[]
    }
}
```

### 4. 更新部门信息

更新某个部门的数据信息

#### URL

`/departments/{department_id}`

#### 请求方式

`PUT`

#### 请求参数

|   参数名称    | 是否必须 | 参数类型 |   参数位置   |      参数说明      |
| :-----------: | :------: | :------: | :----------: | :----------------: |
| department_id |    Y     | Integer  |   url path   |       部门ID       |
|     name      |    Y     |  String  | request data |      部门名称      |
|    parent     |    Y     |  String  | request data | 部门的上级部门名称 |

示例：

```json
{"name":"测试组", "parent":"平台架构组"}
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":{
        "id":11,
        "name":"测试组",
        "parent":{
            "id":4,
            "name":"平台架构组"
        },
        "subs":[]
    }
}
```

### 5. 删除部门

删除某个部门信息

#### URL

`/departments/{department_id}`

#### 请求方式

`DELETE`

#### 请求参数

|   参数名称    | 是否必须 | 参数类型 | 参数位置 | 参数说明 |
| :-----------: | :------: | :------: | :------: | :------: |
| department_id |    Y     | Integer  | url path |  部门ID  |

示例：

```
/departments/10
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":[]
}
```

### 6. 获取部门的上级部门

查看某一部门的上级部门信息

#### URL

`/departments/{department_id}/parent`

#### 请求方式

`GET`

#### 请求参数

|   参数名称    | 是否必须 | 参数类型 | 参数位置 | 参数说明 |
| :-----------: | :------: | :------: | :------: | :------: |
| department_id |    Y     | Integer  | url path |  部门ID  |

示例：

```
/departments/10/parent
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":{
        "id":9,
        "name":"丹炉组"
    }
}
```

### 7. 获取部门的子部门

获取某一部门的所有子部门信息

#### URL

`/departments/{department_id}/subs`

#### 请求方式

`GET`

#### 请求参数

|   参数名称    | 是否必须 | 参数类型 |    参数位置    | 参数说明 |
| :-----------: | :------: | :------: | :------------: | :------: |
| department_id |    Y     | Integer  |    url path    |  部门ID  |
|     page      |    N     | Integer  | url path query |   页码   |
|   per_page    |    N     | Integer  | url path query | 每页条数 |
|     limit     |    N     | Integer  | url path query | 指定数量 |
|    offset     |    N     | Integer  | url path query |  偏移量  |

示例：

```
/departments/1/subs?page=1&per_page=10
/departments/1/subs?limit=5&offset=3
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":[
        {
            "id":7,
            "name":"数据研发组"
        },
        {
            "id":8,
            "name":"web开发组"
        }
    ]
}
```

### 8. 获取同级部门

获取某一部门的同级部门信息

#### URL

`/departments/{department_id}/siblings`

#### 请求方式

`GET`

#### 请求参数

|   参数名称    | 是否必须 | 参数类型 |    参数位置    | 参数说明 |
| :-----------: | :------: | :------: | :------------: | :------: |
| department_id |    Y     | Integer  |    url path    |  部门ID  |
|     page      |    N     | Integer  | url path query |   页码   |
|   per_page    |    N     | Integer  | url path query | 每页条数 |
|     limit     |    N     | Integer  | url path query | 指定数量 |
|    offset     |    N     | Integer  | url path query |  偏移量  |

示例：

```
/departments/1/siblings?page=1&per_page=10
/departments/1/siblings?limit=5&offset=3
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":[
        {
            "id":7,
            "name":"数据研发组"
        },
        {
            "id":8,
            "name":"web开发组"
        }
    ]
}
```

## 员工管理接口

### 1. 获取所有员工列表

#### URL

`/employees`

#### 请求方式

`GET`

#### 请求参数

|  参数名称  | 是否必须 | 参数类型 |    参数位置    |   参数说名   |
| :--------: | :------: | :------: | :------------: | :----------: |
|    page    |    N     | Integer  | url path query |     页码     |
|  per_page  |    N     | Integer  | url path query |   每页条数   |
|   limit    |    N     | Integer  | url path query |   指定数量   |
|   offset   |    N     | Integer  | url path query |    偏移量    |
|    name    |    N     |  String  | url path query | 根据姓名过滤 |
|   gender   |    N     |  String  | url path query | 根据性别过滤 |
| department |    N     |  String  | url path query | 根据部门过滤 |

示例：

```
/employees?name=xxx&gender=男&page=1&per_page=10
/employees?department=前端组&limit=5&offset=3
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":[
        {
            "id":1,
            "name":"赵明",
            "gender":"男",
            "department":"数据研发组"
        },
        {
            "id":2,
            "name":"马宁",
            "gender":"男",
            "department":"数据研发组"
        }
    ]
}
```

### 2. 添加员工

添加员工信息

#### URL

`/employees`

#### 请求方式

`POST`

#### 请求参数

|  参数名称  | 是否必须 | 参数类型 |   参数位置   |     参数说明     |
| :--------: | :------: | :------: | :----------: | :--------------: |
|    name    |    Y     |  String  | request data |     员工姓名     |
|   gender   |    Y     |  String  | request data |     员工性别     |
| department |    Y     |  String  | request data | 员工所在部门名称 |

示例：

```json
{"name":"张三", "gender":"男", "department":"前端开发组"}
```

#### 成功响应示例

```json
{
    "code":201,
    "msg":"created",
    "data":{
        "id":22,
        "name":"张三",
        "gender":"男",
        "department":"前端开发组"
    }
}
```

### 3. 查看单个员工信息

获取单个员工的信息

#### URL

`/employees/{employee_id}`

#### 请求方式

`GET`

#### 请求参数

|  参数名称   | 是否必须 | 参数类型 |   参数位置   |     参数说明     |
| :---------: | :------: | :------: | :----------: | :--------------: |
| employee_id |    Y     | Integer  |   url path   |      员工ID      |

示例：

```
/employees/22
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":{
        "id":22,
        "name":"张三",
        "gender":"男",
        "department":"前端开发组"
    }
}
```

### 4.  更新员工信息

更新某个员工的信息

#### URL

`/employees/{employee_id}`

#### 请求方式

`PUT`

#### 请求参数

|  参数名称   | 是否必须 | 参数类型 |   参数位置   |     参数说明     |
| :---------: | :------: | :------: | :----------: | :--------------: |
| employee_id |    Y     | Integer  |   url path   |      员工ID      |
|    name     |    Y     |  String  | request data |     员工姓名     |
|   gender    |    Y     |  String  | request data |     员工性别     |
| department  |    Y     |  String  | request data | 员工所在部门名称 |
示例：

```json
{"name":"张三", "gender":"女", "department":"前端开发组"}
```


#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":{
        "id":22,
        "name":"张三",
        "gender":"女",
        "department":"前端开发组"
    }
}
```

### 5. 删除某个员工

删除某个员工信息

#### URL

`/employees/{employee_id}`

#### 请求方式

`DELETE`

#### 请求参数

|  参数名称   | 是否必须 | 参数类型 | 参数位置 | 参数说明 |
| :---------: | :------: | :------: | :------: | :------: |
| employee_id |    Y     | Integer  | url path |  员工ID  |

示例：

```
/employees/22
```

#### 成功响应示例

```json
{
    "code":200,
    "msg":"success",
    "data":[]
}
```

