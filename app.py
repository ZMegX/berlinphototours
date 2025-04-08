from flask import Flask
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)

tours = {
    1: {
        "name": "Discover the street art in Berlin",
        "description": "Discover the most beautiful street art in Berlin, from local artists to international masters.",
        "price": 25.00,
        "amount": 10,
        "image_url": "https://example.com/images/street_art.jpg"
    },
    2: {
        "name": "Discover the cityscape in Berlin",
        "description": "Experience the bustling cityscape in Berlin, from the vibrant streets to the serene hills.",
        "price": 30.00,
        "amount": 10,
        "image_url": "https://example.com/images/cityscape.jpg"
    },
    3: {
        "name": "Discover the nightlife in Berlin",
        "description": "Savor the lively nightlife in Berlin, from the charming clubs to the bustling bars.",
        "price": 20.00,
        "amount": 10,
        "image_url": "https://example.com/images/nightlife.jpg"
    }

}
@app.route('/tours')
def show_tours():
    return render_template('tours.html', tours=tours)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/order")
def order_form():
    return render_template("order.html")

@app.errorhandler(404) 
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404

def internal_error(error):
    return render_template('errors/500.html', error=error), 500