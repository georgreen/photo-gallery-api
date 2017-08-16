"""Entry point for app, contain commands to configure and run the app."""
import os
from flask_script import Manager
from flask_migrate import Migrate

from config import configuration
from app import create_app
from models import db

app = create_app(enviroment=os.environ.get('APP_SETTINGS') or "Development")
manager = Manager(app)

if __name__ == "__main__":
    manager.run()