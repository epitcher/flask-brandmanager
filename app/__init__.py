from flask import Flask, send_from_directory
from jinja2 import FileSystemLoader, ChoiceLoader

def create_app():
    app = Flask(__name__)

    # Create loaders for individual module template dirs
    loader_uploader = FileSystemLoader('app/modules/admin/views')
    loader_user = FileSystemLoader('app/modules/user/views')

    # Combine the loaders using ChoiceLoader
    app.jinja_loader = ChoiceLoader([loader_uploader, loader_user])

    from .main import main

    from .modules.user.controllers.AccountController import account_controller
    from .modules.user.controllers.SearchController import search_controller
    from .modules.user.controllers.StorageController import storage_controller

    from .modules.admin.controllers.AnalyticsController import analytics_controller
    from .modules.admin.controllers.AdminStorageController import admin_storage_controller
    from .modules.admin.controllers.UploadController import upload_controller

    app.register_blueprint(main)

    # Module "user" defacto default module
    app.register_blueprint(account_controller)
    app.register_blueprint(search_controller)
    app.register_blueprint(storage_controller)

    # Module "admin"
    app.register_blueprint(analytics_controller)
    app.register_blueprint(admin_storage_controller)
    app.register_blueprint(upload_controller)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    return app
