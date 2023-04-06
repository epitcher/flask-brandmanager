from flask import Blueprint, jsonify, render_template
from flask_login import login_required


admin_storage_controller = Blueprint('admin_storage_controller', __name__)

@admin_storage_controller.route('/admin_storage')
@login_required
def index():
    return render_template('admin_storage/index.html')

# ... (other routes)
