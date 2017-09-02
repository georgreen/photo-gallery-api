"""Module for public endpoints."""
from flask import request

from flask_restplus import Resource, reqparse

try:
    from models import (Picture, Fashion, FineArt, Composite,
                        Conceptual, BeautyGlamour, Portrait,
                        LifeStyle)
    from .base import create_art_work
except ImportError:
    from photo_app.models import (Picture, Fashion, FineArt, Composite,
                                  Conceptual, BeautyGlamour, Portrait,
                                  LifeStyle)
    from photo_app.api.base import create_art_work

# parser object, used to get data passed in in request body
parser = reqparse.RequestParser()

# constant dict: mapper of string to model class
category_types = {'fashion': Fashion, 'beauty_glamour': BeautyGlamour,
                  'portraits': Portrait, 'fine_arts': FineArt,
                  'conceptuals': Conceptual, 'composites': Composite,
                  'life_styles': LifeStyle}


class Categories(Resource):
    """Resources for All serve all pictures in Categories."""

    def get(self):
        """Get art from all categories."""
        response = {}

        for value in category_types:
            response[value] = [art.serialize()
                               for art in Picture.query.filter_by(
                                   type=value).limit(10).all()]
        return response, 200

    def post(self):
        """Create art in a category."""
        parser.add_argument('name', required=True,
                            help='required and must be a string')
        parser.add_argument('category', required=True,
                            help='required and must be a string')
        args = parser.parse_args()

        category = args.get('category')
        name = args.get('name')
        if category not in category_types:
            return {"message": f"category: {category} is not avaiable"}, 400

        new_art = create_art_work(name, category_types[category])
        if not new_art:
            msg = f"Art work: {name} in {category} was not created"
            return {"message": msg}, 500
        return {"new_art": new_art.serialize()}


class Category(Resource):
    """Resource for a specific category of pictures."""

    def get(self, name=None, id=None, image_name=None):
        """Get art from a specific category."""
        response = []
        if name not in category_types:
            return {"message": "The category is not avaiable."}, 400

        elif name and id:
            response = [art.serialize()
                        for art in Picture.query.filter_by(
                            type=name).filter_by(uuid=id).all()]
        elif name and image_name:
            response = [art.serialize()
                        for art in Picture.query.filter_by(
                            type=name).filter_by(name=image_name).all()]
        elif name:
            response = [art.serialize()
                        for art in Picture.query.filter_by(
                                  type=name).all()]

        return response, 200


class Project(Resource):
    """Resources for projects."""

    def get(self, project_name, name):
        """Get project from collection."""
        response = []

        if name in category_types:
            response = [art.serialize()
                        for art in Picture.query.filter_by(
                        type=name).filter_by(project=project_name).all()]
        elif name == 'all':
            response = [art.serialize()
                        for art in Picture.query.filter_by(
                            project=project_name).all()]
        elif name not in category_types:
            return {"message": "The category is not avaiable."}, 400

        return response, 200
