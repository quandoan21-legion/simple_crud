from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
secret_key = "simple_crud"


def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'
    app.config.from_object('config.Config')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login_controller.login'

    with app.app_context():
        from app.models import teammate_model  # Import models within the app context
        db.create_all()
    from app.controllers import teammate_controller
    from app.models.teammate_model import teammates
    from app.controllers import new_teammate_controller
    from app.controllers import index_controller
    from app.controllers import teammate_info_controller
    from app.controllers import login_controller

    app.register_blueprint(teammate_controller.teammate_controller)
    app.register_blueprint(new_teammate_controller.new_teammate_controller)
    app.register_blueprint(index_controller.index_controller)
    app.register_blueprint(teammate_info_controller.teammate_info_controller)
    app.register_blueprint(login_controller.login_controller)


    @login_manager.user_loader
    def load_user(user_id):
        return teammates.query.get(int(user_id))

    return app
