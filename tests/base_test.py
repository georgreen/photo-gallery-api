"""Module to house setup, teardown and utility class for testing."""

from unittest import TestCase

from photo_app.app import create_app
from photo_app.models import db, Fashion, Tag


class BaseTestCase(TestCase):
    """Contain utility required for testing."""

    def setUp(self):
        """Setup function to configure test enviroment."""
        self.app = create_app('Testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

        # mock fashion instance
        self.fashion = Fashion(path="/img/fashion.jpeg",
                               name="test-fashion-instance",
                               project="wet forest",
                               meta_data={
                                   "description": "Go green!",
                                   "date_created": "12/01/1997",
                                   "resolution": "720X1800",
                                   "time": "noon",
                                   "tags":
                                   ["lifestyle", "composite", "potrait"]
                                   })
        # mock tag instance
        self.tag = Tag(name="test-tag-instance")

    def tearDown(self):
        """Clean up after every test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
