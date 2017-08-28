"""Module contain tests for models."""
from photo_app.models import Fashion, Picture, Tag

from .base_test import BaseTestCase


class TestFashion(BaseTestCase):
    """Contain test for Fashion Model."""

    def test_create_fashion_object(self):
        """Test Fashion objects can be created."""
        fashion = Fashion(path="/img/fashion.jpeg",
                          name="newfashionitem",
                          project="desert storm",
                          meta_data={
                              "description": "All winds go!",
                              "date_created": "12/01/1997",
                              "resolution": "720X1800",
                              "time": "noon",
                              "tags": ["lifestyle", "composite"]
                              })
        self.assertTrue(fashion.save())
        new_fashion_instance = Picture.query.filter_by(
            type="fashion").filter_by(name="newfashionitem").first()
        self.assertTrue(new_fashion_instance == fashion)

    def test_delete_fashion_object(self):
        """Test fashion object can be deleted."""
        self.assertTrue(self.fashion.save())
        new_fashion_instance = Picture.query.filter_by(
            type="fashion").filter_by(name="test-fashion-instance").first()
        self.assertTrue(new_fashion_instance)
        self.assertTrue(new_fashion_instance.delete())
        new_fashion_instance = Picture.query.filter_by(
            type="fashion").filter_by(name="test-fashion-instance").first()
        self.assertFalse(new_fashion_instance)


class TestTag(BaseTestCase):
    """Contain tests fro Tag model."""

    def test_create_tag_object(self):
        """Test tag instance can be created."""
        fashion_tag = Tag(name="fashion")
        self.assertTrue(fashion_tag.save())
        tag_instance = Tag.query.filter_by(name="fashion").first()
        self.assertTrue(tag_instance == fashion_tag)

    def test_add_tag_to_picture_models(self):
        """Test tags can be added to picture models."""
        self.assertTrue(self.tag.save())
        self.assertTrue(self.fashion.save())

        self.fashion.tags.append(self.tag)
        new_fashion_instance = Picture.query.filter_by(
            type="fashion").filter_by(name="test-fashion-instance").first()
        self.assertTrue(new_fashion_instance.tags == self.fashion.tags)


class TestBeautyGlamour(BaseTestCase):
    """Test BeautyGlamour model."""

    def test_create_BeautyGlamour_object(self):
        pass


class TestPortrait(BaseTestCase):
    """Test Portait model."""

    def test_create_Portrait_object(self):
        pass


class TestFineArt(BaseTestCase):
    """Test FineArt model."""

    def test_create_FineArt_object(self):
        pass
