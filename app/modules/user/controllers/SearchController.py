from flask import Blueprint, jsonify, render_template
from flask_login import login_required

search_controller = Blueprint('search_controller', __name__)

product_list = [
        {"id": 1, "name": "Product 1"},
        {"id": 2, "name": "Product 2"},
        {"id": 3, "name": "Product 3"},
        {"id": 4, "name": "Product 4"},
        {"id": 5, "name": "Product 5"},
    ]

@search_controller.route('/search')
@login_required
def index():
    return render_template('search/index.html')

@search_controller.route('/products')
@login_required
def products():
    return jsonify(product_list)

# Item page
@search_controller.route('/product/<int:product_id>')
@login_required
def product(product_id):
    product = next((a for a in products if a["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return "Product not found", 404

# ... (other routes)
