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
    return render_template("products.html", products=filtered_items)


@app.route('/tours/<sku>')
def item(sku):
    return render_template("tours.html", product=items_in_stock[sku], sku=sku)


@app.route('/order/<sku>', methods=["POST"])
def order(sku):
    item = items_in_stock[sku]
    if item["amount"] > 0:
        item["amount"] -= 1
        return render_template("confirmation.html")
    else:
        return render_template("item_not_in_stock.html")

@app.route('/admin/tours/<sku>', methods=["GET"])
def edit_item(sku):
    print(items_in_stock)
    
    if sku == items_in_stock.keys():
        product=items_in_stock[sku]
    else:
        product=None

    print("Edit product details:", product)

    return render_template("edit_item.html", product=product, sku=sku)

@app.route('/admin/tours/<sku>', methods=["POST"])
def set_item(sku):
    existing_item = items_in_stock.get(sku)
    if existing_item:
        name = request.form.get("name", existing_item["name"])
        description = request.form.get("description", existing_item["description"])
        price = float(request.form.get("price", existing_item["price"]))
        amount = int(request.form.get("amount", existing_item["amount"]))
        image_url = request.form.get("image_url", existing_item["image_url"])
    else:
        name = request.form["name"]
        description = request.form["description"]
        #price = float(request.form["price"])
        #amount = int(request.form["amount"])
        #image_url = request.form["image_url"]
        price = 10
        amount = 5
        image_url = "https://ae01.alicdn.com/kf/HTB1dbleX_zGK1JjSspbq6zHpFXaE/Men-Shirt-2017-Spring-New-Brand-Business-Men-s-Slim-Fit-Dress-Shirt-Male-Long-Sleeves.jpg"


    items_in_stock[sku] = {
        "name": name,
        "description": description,
        "price": price,
        "amount": amount,
        "image_url": image_url,
    }
    return redirect(url_for("tours"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tours")
def tours():
    return render_template("tours.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")