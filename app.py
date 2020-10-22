from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from views import index_blu,passport_blu
from models import db

app = Flask(__name__)

# 加载配置
app.config.from_pyfile("config.ini")

# 创建蓝图,且注册到app
app.register_blueprint(index_blu)
app.register_blueprint(passport_blu)

db.init_app(app)
# 添加数据库迁移工具
manager = Manager(app)
# 生成migrate对象，用来数据库迁移
migrate = Migrate(app, db)
# 添加db命令
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
