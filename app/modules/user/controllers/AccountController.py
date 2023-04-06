from flask import Blueprint, jsonify, render_template

account_controller = Blueprint('account_controller', __name__)

@account_controller.route('/account')
def index():
    return render_template('analytics/index.html')

# ... (other routes)
