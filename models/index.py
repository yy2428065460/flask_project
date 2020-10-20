from . import db


class User(db.Model):
    # 对应Mysql中数据库的名字
    __tablename__ = 'user'

    # 创建字段
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
