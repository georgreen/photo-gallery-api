"""Entry point for app, contain commands to configure and run the app."""
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, prompt_bool

from app import create_app
from models import (Admin, ArtWork, BeautyGlamour, Composites, Conceptual,
                    Fashion, FineArt, LifeStyle, db)

app = create_app(enviroment=os.environ.get('APP_SETTINGS') or "Development")
manager = Manager(app)
migrate = Migrate(app, db)


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
                ArtWork=ArtWork,
                Admin=Admin,
                BeautyGlamour=BeautyGlamour,
                Composites=Composites,
                Conceptual=Conceptual,
                Fashion=Fashion,
                FineArt=FineArt,
                LifeStyle=LifeStyle)


manager.add_command("shell", Shell(make_context=shell))
manager.add_command("database", MigrateCommand)


if __name__ == "__main__":
    manager.run()
