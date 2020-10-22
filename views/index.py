from flask import render_template,session
from . import index_blu


@index_blu.route("/")
def index():
    # 查询用户是否已经登录
    user_id = session.get("user_id", 0)
    nick_name = session.get("nick_name", "")

    return render_template("index.html",nick_name=nick_name)


@index_blu.route("/index/gallery.html")
def gallery():
    return render_template("gallery.html")


@index_blu.route("/index/about-us.html")
def about():
    return render_template("about-us.html")
