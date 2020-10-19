from flask import Flask

from views import  index_blu

app = Flask(__name__)

# 创建蓝图
app.register_blueprint(index_blu)


if __name__ == '__main__':
    app.run()
