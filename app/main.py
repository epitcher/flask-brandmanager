from flask import Blueprint, jsonify, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

# ... (other routes)
