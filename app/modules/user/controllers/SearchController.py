from flask import Blueprint, jsonify, render_template

search_controller = Blueprint('search_controller', __name__)

@search_controller.route('/search')
def index():
    return render_template('search/index.html')

# ... (other routes)
