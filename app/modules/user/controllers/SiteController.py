from flask import Blueprint, jsonify, render_template, send_from_directory
from flask_login import login_required

site_controller = Blueprint('site_controller', __name__)

@site_controller.route('/')
@login_required
def index():
    return render_template('site/index.html')


# ... (other routes)
