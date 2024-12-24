from flask import Flask

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)

    # Configuration (if needed, add your configuration here)
    app.config['DEBUG'] = True

    # Register blueprints (if any)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
