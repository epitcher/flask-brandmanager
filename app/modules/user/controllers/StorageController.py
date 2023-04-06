from flask import Blueprint, jsonify, render_template
from flask_login import login_required

storage_controller = Blueprint('storage_controller', __name__)

@storage_controller.route('/storage')
@login_required
def index():
    return render_template('storage/index.html')

# ... (other routes)
