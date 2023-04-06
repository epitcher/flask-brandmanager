from flask import Blueprint, jsonify, render_template
from flask_login import login_required

upload_controller = Blueprint('upload_controller', __name__)

@upload_controller.route('/upload')
@login_required
def index():
    return render_template('upload/index.html')

# ... (other routes)
