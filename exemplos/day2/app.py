from flask import Flask, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["APP_NAME"] = "Meu Blog"
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog"

mongo = app.mongo = PyMongo(app)

@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config["APP_NAME"]}"


@app.route("/")
def index():
    posts = mongo.db.posts.find()
    content_url = url_for("read_content", slug="qualquer-coisa")
    return (
        f"<h1>Boas vindas a {app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Leia um post</a>"
        f"<hr/>"
        f"{list(posts)}"
    )

@app.route("/<slug>")
def read_content(slug):
    index_url = url_for("index")
    return f"<h1>{slug}</h1><a href='{index_url}'>Voltar ao inicio</a>"

