from flask import render_template,session

from models import db
from . import index_blu
from models.index import Team, Shop, Category


@index_blu.route("/")
def index():
    # 查询用户是否已经登录
    user_id = session.get("user_id", 0)
    nick_name = session.get("nick_name", "")

    return render_template("index.html", nick_name=nick_name)


@index_blu.route("/index/gallery.html")
def gallery():
    return render_template("gallery.html")


@index_blu.route("/index/about-us.html")
def about():
    return render_template("about-us.html")


@index_blu.route("/index/team.html")
def team_data():
    team = db.session.query(Team).filter().all()
    team_id = session.get("id")
    member_name = session.get("member_name")
    skill = session.get("skill")
    avatar_url = session.get("avatar_url")
    return render_template("team.html",team=team, team_id=team_id, member_name=member_name, skill=skill,avatar_url=avatar_url)


@index_blu.route("/index/shop.html")
def shop():
    shops = db.session.query(Shop).filter().all()
    shops_id = session.get("id")
    price = session.get("price")
    pic_url = session.get("pic_url")

    categorys = db.session.query(Category).filter().all()
    for i in categorys:
        print(i.id)
    c_id = session.get('id')
    category_name = session.get('category_name')

    return render_template("shop.html", shops=shops, shops_id=shops_id, price=price, pic_url=pic_url, categorys=categorys, c_id=c_id, category_name=category_name)


@index_blu.route("/index/shop-details.html")
def shop_details():
    return render_template("shop-details.html")


@index_blu.route("/index/contact-us.html")
def contact_us():
    return render_template("contact-us.html")