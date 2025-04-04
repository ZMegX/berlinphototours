from flask import Flask
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)

items_in_stock = {
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
@app.route('/products/')
def products():
    search_term = request.args.get("q", "")
    filtered_items = []
    for sku, item in items_in_stock.items():
        if search_term.lower() in item["description"].lower():
            filtered_items.append((sku, item))
    return render_template("product.html", products=filtered_items)


@app.route('/tours/<sku>')
def item(sku):
    return render_template("tours.html", items_in_stock=items_in_stock)


@app.route('/order/<sku>', methods=["POST"])
def order(sku):
    item = items_in_stock[sku]
    if item["amount"] > 0:
        item["amount"] -= 1
        return render_template("confirmation.html")
    else:
        return render_template("item_not_in_stock.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tours/")
def tours():
    return render_template("tours.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")