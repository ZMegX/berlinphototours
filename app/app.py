print("App is being loaded...")

from flask import Flask
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)


tours = {
    1: {
        "name": "Discover the street art in Berlin",
        "description": "Discover the most beautiful street art in Berlin, from local artists to international masters.",
        "price": 25.00,
        "amount": 10,
        "image_url": "https://i.postimg.cc/YqVM57jD/IMG-0948.jpg"
    },
    2: {
        "name": "Discover the cityscape in Berlin",
        "description": "Experience the bustling cityscape in Berlin, from the vibrant streets to the serene hills.",
        "price": 30.00,
        "amount": 5,
        "image_url": "https://i.postimg.cc/651KqHb9/museum-island-berlin.jpg"
    },
    3: {
        "name": "Discover the nightlife in Berlin",
        "description": "Savor the lively nightlife in Berlin, from the charming clubs to the bustling bars.",
        "price": 20.00,
        "amount": 8,
        "image_url": "https://i.postimg.cc/rwrMcHrV/nightlife-berlin-tour.jpg"
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

@app.route('/order')
def order_form():
    return render_template('order.html')

#when the user clicks on the submit button of the form in the order.html
#flask is requesting the value below
#if True the orderReceived.html the user is directed to orderReceived.html
@app.route('/submit', methods=['POST'])
def submit_order():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    return render_template('orderReceived.html', name=name, email=email, phone=phone)

@app.errorhandler(404) 
def not_found_error(error):
    return render_template('errors/404.html', error=error), 404

@app.errorhandler(500) 
def internal_error(error):
    return render_template('errors/500.html', error=error), 500

if __name__ == "__main__":
    app.run()