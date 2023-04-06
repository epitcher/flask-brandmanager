from flask import Blueprint, jsonify, render_template
from flask_login import login_required

analytics_controller = Blueprint('analytics_controller', __name__)

@analytics_controller.route('/analytics')
@login_required
def index():
    return render_template('analytics/index.html')

# ... (other routes)
