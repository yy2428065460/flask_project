from flask import render_template,session,request,redirect,url_for

from models import db
from . import index_blu
from models.index import Team, Shop, Category, User


@index_blu.route("/")
def index():
    # 查询用户是否已经登录
    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    user_avatar_url = session.get('avatar_url')
    print(user_avatar_url)
    return render_template("index.html", nick_name=nick_name, avatar_url=user_avatar_url, user=user)


@index_blu.route("/index/gallery.html")
def gallery():
    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    user_avatar_url = session.get('avatar_url')
    print(user_avatar_url)
    return render_template("gallery.html", nick_name=nick_name, avatar_url=user_avatar_url, user=user)


@index_blu.route("/index/about-us.html")
def about():
    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    avatar_url = session.get('avatar_url')
    print(avatar_url)
    return render_template("about-us.html", nick_name=nick_name, avatar_url=avatar_url, user=user)


@index_blu.route("/index/team.html")
def team_data():
    team = db.session.query(Team).filter().all()
    team_id = session.get("id")
    member_name = session.get("member_name")
    skill = session.get("skill")
    avatar_url = session.get("avatar_url")
    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    user_avatar_url = session.get('avatar_url')
    return render_template("team.html",team=team, team_id=team_id, member_name=member_name, skill=skill,avatar_url=avatar_url, user=user, nick_name=nick_name, user_avatar_url=user_avatar_url)


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

    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    user_avatar_url = session.get('avatar_url')

    return render_template("shop.html", shops=shops, shops_id=shops_id, price=price, pic_url=pic_url, categorys=categorys, c_id=c_id, category_name=category_name, user_avatar_url=user_avatar_url, user=user, nick_name=nick_name)


@index_blu.route("/index/shop-details", methods=['GET', 'POST'])
def shop_details():
    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    user_avatar_url = session.get('avatar_url')
    return render_template("shop-details.html", user=user, nick_name=nick_name, user_avatar_url=user_avatar_url)


@index_blu.route("/index/contact-us.html")
def contact_us():
    user_id = session.get("user_id", 0)
    user = db.session.query(User).filter(User.id == user_id).first()
    nick_name = session.get("nick_name", "")
    user_avatar_url = session.get('avatar_url')
    return render_template("contact-us.html", user=user, nick_name=nick_name, user_avatar_url=user_avatar_url)


@index_blu.route('/index/user.html')
def user():
    return render_template("user.html")


@index_blu.route('/index/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    return render_template("shopping_cart.html")


@index_blu.route('/index/order', methods=['GET', 'POST'])
def order():
    if request.method=="POST":
        return redirect(url_for('index_blu.commit'))
    else:
        return render_template("order.html")


@index_blu.route('/index/commit', methods=['GET', 'POST'])
def commit():
    print('123')
    return render_template("commit.html")
