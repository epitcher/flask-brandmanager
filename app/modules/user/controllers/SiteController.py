from flask import Blueprint, jsonify, render_template, send_from_directory
from flask_login import login_required

site_controller = Blueprint('site_controller', __name__)

@site_controller.route('/')
@login_required
def index():
    products = [
        {
            "id": 1,
            "name": "Product A",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 9.99,
            "image_url": "https://example.com/product-a.jpg"
        },
        {
            "id": 2,
            "name": "Product B",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 14.99,
            "image_url": "https://example.com/product-b.jpg"
        },
        {
            "id": 3,
            "name": "Product C",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 24.99,
            "image_url": "https://example.com/product-c.jpg"
        },
        {
            "id": 4,
            "name": "Product D",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 19.99,
            "image_url": "https://example.com/product-d.jpg"
        },
        {
            "id": 5,
            "name": "Product E",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 12.99,
            "image_url": "https://example.com/product-e.jpg"
        },
        {
            "id": 6,
            "name": "Product F",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 29.99,
            "image_url": "https://example.com/product-f.jpg"
        },
        {
            "id": 7,
            "name": "Product G",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 8.99,
            "image_url": "https://example.com/product-g.jpg"
        },
        {
            "id": 8,
            "name": "Product H",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 11.99,
            "image_url": "https://example.com/product-h.jpg"
        },
        {
            "id": 9,
            "name": "Product I",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 17.99,
            "image_url": "https://example.com/product-i.jpg"
        },
        {
            "id": 10,
            "name": "Product J",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 22.99,
            "image_url": "https://example.com/product-j.jpg"
        },
        {
            "id": 11,
            "name": "Product K",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 15.99,
            "image_url": "https://example.com/product-k.jpg"
        },
        {
            "id": 12,
            "name": "Product L",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 7.99,
            "image_url": "https://example.com/product-l.jpg"
        },
        {
            "id": 13,
            "name": "Product M",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "price": 13.99,
            "image_url": "https://example.com/product-m.jpg"
        }]

    return render_template('site/index.html', products=products)


# ... (other routes)
