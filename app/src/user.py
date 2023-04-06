from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, username, password, authenticated):
        self.id = username
        self.password = password
        self.authenticated = authenticated


users = {
    "user": {
        "password": generate_password_hash("user"),
        "authenticated": False
    },
    "admin": {
        "password": generate_password_hash("password"),
        "authenticated": False
    }
}
