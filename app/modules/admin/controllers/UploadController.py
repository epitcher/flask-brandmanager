from flask import Blueprint, jsonify, render_template

upload_controller = Blueprint('upload_controller', __name__)

@upload_controller.route('/upload')
def home():
    return render_template('upload/index.html')

# ... (other routes)
