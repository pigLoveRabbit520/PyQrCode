# Python二维码识别Web服务
![Test Decode Image](https://github.com/salamander-mh/PyQrCode/workflows/Test%20Decode%20Image/badge.svg?event=push)
[![GitHub](https://img.shields.io/github/license/salamander-mh/PyQrCode)](LICENSE) 


本项目利用[**opencv-python**](https://pypi.org/project/opencv-python/)库和`pyzbar`库。  

Python web框架使用[FastAPI](https://fastapi.tiangolo.com/)


# 使用
```
docker run -it --rm -p 8888:8000 salamandermh/pyqrcode
```
访问`http://localhost:8888`，可以看到用于测试的页面。

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



# 参考文章和说明
* [用OpenCV和Python识别二维码和条形码](https://zhuanlan.zhihu.com/p/40025902)  

使用zbar进行二维码解析，但是标准的zbar不支持`python3`，这个比较坑，还好有个大神在zbar的基础上包装了一下，做了pyzbar的开发包，支持`python2`与`python3`，非常的好用。安装非常容易，windows下一条命令搞定，Linux与Mac OS下面要先安装zbar然后再执行此命令即可。  
在Ubuntu或树莓派上安装Zbar
```shell script
$ sudo apt-get install libzbar0
```
在MacOS系统中安装Zbar
```shell script
$ brew install zbar
```


# cv2模块
`cv2.imread`的`flag`参数说明：
* `cv2.IMREAD_GRAYSCALE` 图片转化为单通道灰度图  
* `cv2.IMREAD_COLOR` 图片转化为三通道`BGR`图片
* `cv2.IMREAD_UNCHANGED` 加载一副彩色图像，同时还会有透明度通道，如png图像
* `cv2.IMREAD_ANYCOLOR` 任何形式的图片格式都直接读入
* `cv2.IMREAD_ANYDEPTH` 若输入图片是16或32位深度图直接读入，否则转化位8位深度图
