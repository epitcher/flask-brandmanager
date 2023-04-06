from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user

account_controller = Blueprint('account_controller', __name__)

@account_controller.route('/account')
@login_required
def index():
    return render_template('account/index.html', user=current_user)


# ... (other routes)
