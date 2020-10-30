from datetime import datetime

from . import db


class Collection(db.Model):

    __tablename__ = "collection"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)  # 新闻编号
    shop_id = db.Column(db.Integer, db.ForeignKey("shop.id"), primary_key=True)  # 分类编号
    create_time = db.Column(db.DateTime, default=datetime.now)  # 收藏创建时间


class User(db.Model):
    """用户"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    avatar_url = db.Column(db.String(256))  # 用户头像路径
    create_time = db.Column(db.DateTime, default=datetime.now)  # 注册时间
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    is_admin = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(512))  # 用户签名
    gender = db.Column(  # 性别
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN"
    )
    collection_news = db.relationship("Shop",
                                      secondary=Collection.__table__,
                                      backref=db.backref('collected_user', lazy='dynamic'),
                                      lazy='dynamic')


class Team(db.Model):
    """护理团队"""
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)  # 成员编号
    member_name = db.Column(db.String(32), unique=True, nullable=False)  # 成员姓名
    member_mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    skill = db.Column(db.String(128))  # 职业技能
    detail = db.Column(db.String(256))
    avatar_url = db.Column(db.String(255))


class Shop(db.Model):
    """商品表"""

    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(32), unique=True, nullable=False)  # 商品名
    price = db.Column(db.String(11), unique=True, nullable=False)  # 价格
    pic_url = db.Column(db.String(255))  # 商品图片路径
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))


class Category(db.Model):
    """分类表"""

    __tablename__ = "category"

    id = db.Column(db.Integer, unique=True, primary_key=True)  # 分类编号
    category_name = db.Column(db.String(64), nullable=False)  # 分类名


