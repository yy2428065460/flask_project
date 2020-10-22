from flask import render_template
from . import index_blu


@index_blu.route("/")
def index():
    return render_template("index.html")


@index_blu.route("/index/gallery.html")
def gallery():
    return render_template("gallery.html")

