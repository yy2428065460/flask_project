import hashlib
import time
from flask import jsonify, session, request, render_template, redirect, url_for

from . import user_blu
from models import db
from models.index import User


@user_blu.route("/user/center")
def user_center():
    user_id = session.get("user_id")
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name")

    # 如果用户未登录，禁止访问用户中心
    if not nick_name:
        return redirect(url_for('index_blu.index'))

    return render_template("user.html", nick_name=nick_name, user=user)


@user_blu.route("/user/user_base_info.html")
def user_base_info():
    return render_template("user_base_info.html")


@user_blu.route("/user/basic", methods=["POST"])
def user_basic():
    # 获取用户的新的信息
    nick_name = request.json.get("nick_name")
    signature = request.json.get("signature")
    gender = request.json.get("gender")

    # 获取当前用户的信息
    user_id = session.get("user_id")

    # 存储到数据库
    user = db.session.query(User).filter(User.id == user_id).first()
    if not user:
        ret = {
            "errno": 4002,
            "errmsg": "没有此用户"
        }

        return jsonify(ret)

    # 如果查询到此用户就修改数据
    user.nick_name = nick_name
    user.signature = signature
    user.gender = gender

    db.session.commit()

    ret = {
        "errno": 0,
        "errmsg": "修改成功..."
    }
    return jsonify(ret)


@user_blu.route("/user/user_pass_info")
def user_pass_info():
    return render_template("user_pass_info.html")


@user_blu.route("/user/password", methods=["POST"])
def user_password():
    # 1. 提取旧密码以及新密码
    new_password = request.json.get("new_password")
    old_password = request.json.get("old_password")

    # 2. 提取当前用户的id
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({
            "errno": 4001,
            "errmsg": "请先登录"
        })

    # 2. 判断旧密码与数据中的当前存储的密码是否相同
    user = db.session.query(User).filter(User.id == user_id, User.password_hash == old_password).first()

    # 3. 如果相同，则修改
    if user:
        user.password_hash = new_password
        db.session.commit()
        ret = {
            "errno": 0,
            "errmsg": "修改成功"
        }

    else:
        ret = {
            "errno": 4004,
            "errmsg": "原密码错误！"
        }

    # 返回json
    return jsonify(ret)


@user_blu.route("/user/user_pic_info.html")
def user_pic_info():
    user_id = session.get("user_id")
    user = db.session.query(User).filter(User.id == user_id).first()
    return render_template("user_pic_info.html", user=user)



@user_blu.route("/user/avatar", methods=['POST'])
def user_avatar():
    f = request.files.get("avatar")
    if f:
        # print(f.filename)
        # 为了防止多个用户上传的图片名字相同，需要将用户的图片计算出一个随机的用户名，防止冲突
        file_hash = hashlib.md5()
        file_hash.update((f.filename + time.ctime()).encode("utf-8"))
        file_name = file_hash.hexdigest() + f.filename[f.filename.rfind("."):]

        avatar_url = file_name

        # 将路径改为static/upload下
        file_name = "./static/images/upload/" + file_name

        # 用新的随机的名字当做图片的名字
        f.save(file_name)

        # 修改数据库中用户的头像链接（注意，图片时不放在数据库中的，数据库中存放的图片的名字或者路径加图片名）
        user_id = session.get("user_id")
        user = db.session.query(User).filter(User.id == user_id).first()
        user.avatar_url = avatar_url
        db.session.commit()

        ret = {
            "errno": 0,
            "errmsg": "成功"
        }
    else:
        ret = {
            "errno": 4003,
            "errmsg": "上传失败"
        }

    return jsonify(ret)


@user_blu.route("/user/user_collection.html")
def user_collection():
    # 获取页码
    page = int(request.args.get("page", 1))
    # 查询用户
    user_id = session.get("user_id")
    user = db.session.query(User).filter(User.id == user_id).first()
    # 查询用户收藏的文章
    paginate = user.collection_news.paginate(page, 2, False)

    return render_template("user_collection.html", paginate=paginate)




