"""Contain Api helpers and base configurations."""
# module solves most of ciclic import errors
from flask_restplus import Api

api = Api(
    title='😝 Photo-Gallery Api 😁',
    version='1.0',
    description="""Photo-gallery Api Endpoint Documentation.""")
