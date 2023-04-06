from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, username, password, authenticated):
        self.id = username
        self.password = password
        self.authenticated = authenticated

users = {
    "user1": {"password": generate_password_hash("password1"), "authenticated": False},
    "user2": {"password": generate_password_hash("password2"), "authenticated": False}
}