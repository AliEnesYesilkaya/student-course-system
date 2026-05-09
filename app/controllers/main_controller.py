from flask import Blueprint


main = Blueprint("main", __name__)


@main.route("/")
def home():

    return "Ana Sayfa"


@main.route("/courses")
def courses():

    return "Dersler Sayfası"


@main.route("/transcript")
def transcript():

    return "Transcript Sayfası"


@main.route("/enrollment")
def enrollment():

    return "Ders Kayıt Sayfası"