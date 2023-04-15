import sys
import os
from flask import Flask, send_from_directory, render_template, redirect, url_for, request, flash
from jinja2 import FileSystemLoader, ChoiceLoader
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .src.user import User, users

def create_app():
    app = Flask(__name__)

    # Create loaders for individual module template dirs
    loader_uploader = FileSystemLoader('app/modules/admin/views')
    loader_user = FileSystemLoader('app/modules/user/views')

    # Combine the loaders using ChoiceLoader
    app.jinja_loader = ChoiceLoader([loader_uploader, loader_user])

    from .modules.user.controllers.SiteController import site_controller
    from .modules.user.controllers.LoginController import login_controller
    from .modules.user.controllers.AccountController import account_controller
    from .modules.user.controllers.SearchController import search_controller
    from .modules.user.controllers.StorageController import storage_controller

    from .modules.admin.controllers.AnalyticsController import analytics_controller
    from .modules.admin.controllers.AdminStorageController import admin_storage_controller
    from .modules.admin.controllers.UploadController import upload_controller

    app.secret_key = 'some_secret_key'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login_controller.login'

    # Module "user" defacto default module
    app.register_blueprint(site_controller)
    app.register_blueprint(login_controller)
    app.register_blueprint(account_controller)
    app.register_blueprint(search_controller)
    app.register_blueprint(storage_controller)

    # Module "admin"
    app.register_blueprint(analytics_controller)
    app.register_blueprint(admin_storage_controller)
    app.register_blueprint(upload_controller)

    @login_manager.user_loader
    def load_user(user_id):
        if user_id in users:
            return User(user_id, users[user_id]['password'], users[user_id]['authenticated'])
        return None

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def not_found_error(error):
        return render_template('500.html'), 500
    
    @app.context_processor
    def helpers():

        def get_javascript_files():
            file_type="js"
            dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', file_type)
            return [f for f in os.listdir(dir) if f.endswith('.' + file_type)]
        
        def get_css_files():
            file_type="css"
            dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', file_type)
            
            file_list = [f for f in os.listdir(dir) if f.endswith('.' + file_type)]
            to_remove = ['styles.css']
            for item in to_remove:
                if item in file_list:
                    file_list.remove(item)

            return file_list

        return dict(
            javascript_files=get_javascript_files(),
            css_files=get_css_files()
        )

    return app
