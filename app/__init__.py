# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the routes and register them with the app
    from . import routes
    app.register_blueprint(routes.bp)

    return app
