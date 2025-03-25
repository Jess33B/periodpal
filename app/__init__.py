from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Register blueprints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .tracker import tracker as tracker_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(tracker_blueprint)

    return app