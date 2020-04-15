# 说明
本项目基于**Python**。拟合走势，利用[**scipy**](https://www.scipy.org/)库的`curve_fit`函数

# 使用
```
docker run -it --rm -p 8888:8000 salamandermh/trend_predict
```

# API

## POST /decode
## 参数
|参数名|必选|类型|说明|
|--- |--- |--- |--- |
|file|是|file|上传的图片|

## 返回示例
```
请求成功
{
    "errno": 0,
    "errmsg": "识别成功",
    "data": [
        "https://u.wechat.com/MAjIIa7vj14B0HonaXPcZMA"
    ]
}

请求错误
{
    "errno": 1,
    "errmsg": "1 validation error for Request
           body -> file
           field required (type=value_error.missing)"
}
```
## 返回参数说明
|参数名|类型|说明|
|--- |--- |--- |
|errno|int|错误码，0：成功；1：失败|
|errmsg|string|错误信息|
|data|array|结果数组，一个图片中可能有多个二维码|


# 环境变量
* `WEB_CONCURRENCY`：设置worker进程数量
