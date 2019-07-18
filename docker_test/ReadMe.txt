一个简单的flask应用制作成镜像并部署到linux服务器上。
详细笔记可参考:
https://blog.csdn.net/u013282737/article/details/85233408
----------------------------------------------------------------------------------------
[root@mylinux docker_test]# tree
.
├── Dockerfile
└── flask_demo
    ├── api_client.py
    ├── api_server.py
    ├── __init__.py
    ├── requirements.txt
    └── test.py

1 directory, 6 files
------------------------------------------------------
[root@mylinux docker_test]# cat Dockerfile 
#基于的基础镜像
FROM python:3

#代码添加到code文件夹
ADD ./flask_demo /usr/src/app

# 设置app文件夹是工作目录
WORKDIR /usr/src/app

# 安装支持
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/usr/src/app/api_server.py" ]
------------------------------------------------------

生成镜像
docker build -t flask_demo_img .

启动容器
docker run -it -p 8060:5001 --name flask_demo_cn flask_demo_img
----------------------------------------------------------------------------------------

requirements.txt
certifi==2019.6.16
chardet==3.0.4
Click==7.0
Flask==1.1.1
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
requests==2.22.0
urllib3==1.25.3
Werkzeug==0.15.4