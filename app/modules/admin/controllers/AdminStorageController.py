from flask import Blueprint, jsonify, render_template

admin_storage_controller = Blueprint('admin_storage_controller', __name__)

@admin_storage_controller.route('/admin_storage')
def index():
    return render_template('admin_storage/index.html')

# ... (other routes)
