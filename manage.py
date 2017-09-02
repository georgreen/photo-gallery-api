"""Entry point for app, contain commands to configure and run the app."""

import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, prompt_bool

from app import create_app
from models import (Admin, BeautyGlamour, Composite, Conceptual, Fashion,
                    FineArt, LifeStyle, Picture, Portrait, Tag, db)

try:
    from .api.base import create_art_work
except ImportError:
    from api.base import create_art_work


app = create_app(enviroment=os.environ.get('APP_SETTINGS') or "Development")
manager = Manager(app)
Migrate(app=app, db=db)


@manager.command
def drop_database():
    """Drop database tables."""
    if prompt_bool("Are you sure you want to lose all your data"):
        try:
            db.drop_all()
            print("Dropped all tables susscefully.")
        except Exception:
            print("Failed, make sure your database server is running!")


@manager.command
def create_database():
    """Create database tables from sqlalchemy models."""
    try:
        db.create_all()
        print("Created tables susscefully.")
    except Exception:
        print("Failed, make sure your database server is running!")


def shell():
    """Make a shell/REPL context available."""
    return dict(app=create_app(),
                db=db,
                Picture=Picture,
                Admin=Admin,
                BeautyGlamour=BeautyGlamour,
                Composite=Composite,
                Conceptual=Conceptual,
                Fashion=Fashion,
                FineArt=FineArt,
                LifeStyle=LifeStyle,
                Portrait=Portrait,
                create_art_work=create_art_work,
                Tag=Tag)


manager.add_command("shell", Shell(make_context=shell))
manager.add_command("database", MigrateCommand)


if __name__ == "__main__":
    manager.run()
