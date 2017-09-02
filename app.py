"""Main app module."""
from flask import Flask, jsonify

from whitenoise import WhiteNoise

try:
    # fix import error in nosetest
    from .config import configuration
    from .models import db
    from .api.base import api, import_resources
except ImportError:
    # fix import error in starting the app
    from config import configuration
    from models import db
    from api.base import api, import_resources


def create_app(enviroment="Development"):
    """Factory Method that creates an instance of the app with the given config.

    Args:
        enviroment (str): Specify the configuration to initilize app with.
    Returns:
        app (Flask): it returns an instance of Flask.
    """
    app = Flask(__name__, static_folder='static')
    app.config.from_object(configuration[enviroment])
    db.init_app(app)

    # setup whitenoise to enable heroku to serve static content
    if enviroment in ["Staging", "Production"]:
        app = WhiteNoise(app, root='/static/img/')

    # used to import dependancies this avoid circular imports
    Categories, Category, Project = import_resources()
    api.add_resource(Categories,
                     '/api/v1.0/category/')

    api.add_resource(Category,
                     '/api/v1.0/category/<string:name>/',
                     '/api/v1.0/category/<string:name>/<int:id>/',
                     '/api/v1.0/category/<string:name>/<string:image_name>/')

    api.add_resource(Project,
                     '/api/v1.0/project/<string:name>/<string:project_name>/')

    # app must be initialized with api after adding the urls
    api.init_app(app)

    # handle default 404 exceptions with a custom response
    @app.errorhandler(404)
    def resource_not_found(error):
        response = jsonify(dict(
            error='Not found',
            message='The requested URL was not found on the server.'))
        response.status_code = 404
        return response

    # handle default 500 exceptions with a custom response
    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify(dict(
            error='Internal server error',
            message="The server encountered an internal error."))
        response.status_code = 500
        return response

    return app
