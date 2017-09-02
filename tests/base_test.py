"""Module to house setup, teardown and utility class for testing."""

from unittest import TestCase

try:
    from app import create_app
    from models import (Fashion, Tag, BeautyGlamour, Portrait,
                        FineArt, db, Admin)
except ImportError:
    from photo_app.app import create_app
    from photo_app.models import (Fashion, Tag, BeautyGlamour, Portrait,
                                  FineArt, db, Admin)


class BaseTestCase(TestCase):
    """Contain utility required for testing."""

    def setUp(self):
        """Setup function to configure test enviroment."""

        self.app = create_app('Testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

        # test client
        self.client = self.app.test_client()

        # mock tag instance
        self.tag = Tag(name="test-tag-instance")
        self.tag_lifestyle = Tag(name="test-tag-lifestyle")
        self.tag_composite = Tag(name="test-tag-composite")
        self.tag_potrait = Tag(name="test-tag-potrait")

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
                                   [self.tag_lifestyle, self.tag_composite,
                                    self.tag_potrait, self.tag]
                                   })
        # mock beauty instance
        self.beauty = BeautyGlamour(path="/img/beuty.jpeg",
                                    name="newbeautyitem",
                                    project="desert storm",
                                    meta_data={
                                      "description": "All winds go!",
                                      "date_created": "12/01/1997",
                                      "resolution": "720X1800",
                                      "time": "noon",
                                      "tags":
                                      [self.tag_lifestyle,
                                       self.tag_potrait, self.tag]
                                    })
        # mock potrait instance
        self.portrait = Portrait(path="/img/image.jpeg",
                                 name="newimageitem",
                                 project="desert storm",
                                 meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags":
                                  [self.tag_composite,
                                   self.tag_potrait, self.tag]
                                  })
        # mock fineArt instance
        self.fine_art = FineArt(path="/img/image.jpeg",
                                name="newimageitem",
                                project="desert storm",
                                meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags":
                                  [self.tag_lifestyle, self.tag_composite,
                                   self.tag_potrait]
                                  })
        # mock Admin
        self.admin = Admin(name="test Admin", password="hardtogeuss")

    def tearDown(self):
        """Clean up after every test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
