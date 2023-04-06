from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from ....src.user import User, users

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/index', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('site_controller.index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and check_password_hash(users[username]['password'], password):
            user = User(username, users[username]['password'], True)
            login_user(user)
            return redirect(url_for('site_controller.index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login/index.html')

@login_controller.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_controller.login'))

@login_controller.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.id}!'
