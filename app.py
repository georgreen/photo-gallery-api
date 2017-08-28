"""Main app module."""
from flask import Flask


def create_app(enviroment="Development"):
    """Factory Method that creates an instance of the app with the given config.

    Args:
        enviroment (str): Specify the configuration to initilize app with.
    Returns:
        app (Flask): it returns an instance of Flask.
    """
    # import dependacies here (avoid's circular import problem in testing)
    from config import configuration
    from models import db
    from api.base import api

    app = Flask(__name__)
    app.config.from_object(configuration[enviroment])
    db.init_app(app)
    api.init_app(app)

    return app
