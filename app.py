from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tours")
def tours():
    return render_template("tours.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")