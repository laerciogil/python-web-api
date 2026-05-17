from flask import Flask, url_for, request

app = Flask(__name__)

app.config["APP_NAME"] = "Meu Blog"

@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config["APP_NAME"]}"


@app.route("/")
def index():
    content_url = url_for("read_content", slug="qualquer-coisa")
    return (
        f"<h1>Boas vindas a {app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Leia um post</a>"
        f"<hr/>"
    )

@app.route("/<slug>")
def read_content(slug):
    index_url = url_for("index")
    return f"<h1>{slug}</h1><a href='{index_url}'>Voltar ao inicio</a>"
