from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')

    # Import routes
    from .routes import auth, main
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    return app