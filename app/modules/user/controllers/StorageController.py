from flask import Blueprint, jsonify, render_template

storage_controller = Blueprint('storage_controller', __name__)

@storage_controller.route('/storage')
def home():
    return render_template('storage/index.html')

# ... (other routes)
