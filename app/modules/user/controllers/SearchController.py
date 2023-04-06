from flask import Blueprint, jsonify, render_template
from flask_login import login_required

search_controller = Blueprint('search_controller', __name__)

@search_controller.route('/search')
@login_required
def index():
    return render_template('search/index.html')

# ... (other routes)
