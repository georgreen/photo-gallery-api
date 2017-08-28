"""Module to house setup, teardown and utility class for testing."""
from unittest import TestCase

from photo_app.app import create_app
from photo_app.models import BeautyGlamour, db


class BaseTestCase(TestCase):
    """Contain utility required for testing."""

    def setUp(self):
        """Setup function to configure test enviroment."""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """Clean up after every test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
