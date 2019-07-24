from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

# --------------------------------------------------------

# #导入Flask扩展
# from flask import Flask
#
# # 创建Flask应用实例
# app = Flask(__name__)
#
# # 定义路由及视图函数
# @app.route('/')
# def hello_world():
#     return 'hello world'
#
#
# # 启动程序
# if __name__ == '__main__':
#     app.run(debug=True)