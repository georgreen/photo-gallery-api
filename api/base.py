"""Contain Api helpers and base configurations."""

import os

from flask import url_for
from flask_restplus import Api

try:
    from models import Picture
except ImportError:
    from photo_app.models import Picture

CURRECT_DIR = os.path.dirname(__file__)

api = Api(
    default='Api',
    default_label="Available Endpoints",
    title='😝 Photo-Gallery Api 😱',
    version='1.0',
    description="""Photo-gallery Api Endpoint Documentation 📚""")


def import_resources():
    """Import local modules here."""
    from .artwork_resources import Categories, Category, Project
    return Categories, Category, Project


def create_art_work(image_name, Category, **meta_data):
    """Factory to create art work in Db."""
    print(CURRECT_DIR)
    path = url_for('static', filename=f'img/{image_name}')
    check_art = Picture.query.filter_by(name=image_name).first()
    exist = os.path.exists(CURRECT_DIR[:4] + path)

    if check_art or exist:
        return False
    art_work = Category(name=image_name,
                        meta_data=meta_data,
                        path=path)
    if art_work.save():
        return art_work
