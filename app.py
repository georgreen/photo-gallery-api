"""Main app module."""
from flask import Flask

from models import db
from api.endpoints import api


def create_app(enviroment="Development"):
    app = Flask(__name__)

    return app