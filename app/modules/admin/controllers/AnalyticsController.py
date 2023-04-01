from flask import Blueprint, jsonify, render_template

analytics_controller = Blueprint('analytics_controller', __name__)

@analytics_controller.route('/analytics')
def home():
    return render_template('analytics/index.html')

# ... (other routes)
