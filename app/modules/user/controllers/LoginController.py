from flask import Blueprint, jsonify, render_template, send_from_directory

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login')
def login():
    return render_template('login/index.html')

# ... (other routes)
