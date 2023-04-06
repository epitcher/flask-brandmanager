from flask import Blueprint, jsonify, render_template
from flask_login import login_required

account_controller = Blueprint('account_controller', __name__)

@account_controller.route('/account')
@login_required
def index():
    return render_template('analytics/index.html')

# ... (other routes)
