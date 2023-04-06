from flask import Blueprint, jsonify, render_template, send_from_directory

site_controller = Blueprint('site_controller', __name__)

@site_controller.route('/')
def index():
    return render_template('site/index.html')


# ... (other routes)
