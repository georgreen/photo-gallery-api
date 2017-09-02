"""Module for endpoint tests."""
import json

from .base_test import BaseTestCase


class EndpointBase(BaseTestCase):
    """Base for endpoints."""

    def setUp(self):
        """Setup for endpoints."""
        BaseTestCase.setUp(self)
        self.fashion.save()
        self.beauty.save()
        self.portrait.save()
        self.fine_art.save()


class TestCategories(EndpointBase):
    """Test categories resource."""

    def test_get_all_categories(self):
        """Test retuns all categories."""
        response = self.client.get('/api/v1.0/category/')
        data = json.loads(response.data)
        self.assertTrue(self.fashion.serialize() == data["fashion"][0])
        self.assertTrue(self.beauty.serialize() == data["beauty_glamour"][0])

    def test_post_new_image(self):
        """Test creating new image."""
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        category = "fashion"
        name = "2.jpg"
        data = json.dumps({"name": name, "category": category})
        response = self.client.post('/api/v1.0/category/',
                                    data=data, headers=self.headers)
        response_data = json.loads(response.data)
        self.assertTrue(response_data["new_art"]["name"] == "2.jpg")

        # test duplictes
        response = self.client.post('/api/v1.0/category/',
                                    data=data, headers=self.headers)
        response_data = json.loads(response.data)
        self.assertTrue(response_data["message"] ==
                        f"Art work: {name} in {category} was not created")

    def test_post_invalid_category(self):
        """Test response for invalid category."""
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        category = "Invalid"
        data = json.dumps({"name": "2.jpg", "category": category})
        response = self.client.post('/api/v1.0/category/',
                                    data=data, headers=self.headers)
        response_data = json.loads(response.data)

        self.assertTrue(response_data["message"] ==
                        f"category: {category} is not avaiable")


class TestCategory(EndpointBase):
    """Test Category resource."""

    def test_get_category(self):
        """Test return a specific category."""
        response = self.client.get('/api/v1.0/category/fashion/')
        data = json.loads(response.data)
        self.assertTrue(self.fashion.serialize() == data[0])

    def test_get_art_by_id(self):
        """Test get art with id."""
        response = self.client.get('/api/v1.0/category/fashion/1/')
        data = json.loads(response.data)
        self.assertTrue(self.fashion.serialize() == data[0])

    def test_get_art_by_name(self):
        """Test get art by name."""
        response = self.client.get('/api/v1.0/category/fashion/'
                                   'test-fashion-instance/')
        data = json.loads(response.data)
        self.assertTrue(self.fashion.serialize() == data[0])

    def test_wrong_category_name(self):
        """Test response for wrong category name."""
        response = self.client.get('/api/v1.0/category/fashions/')
        data = json.loads(response.data)
        self.assertTrue(data["message"] == "The category is not avaiable.")


class TestProject(EndpointBase):
    """Test Project resource."""

    def test_get_category_project(self):
        """Test response for get category project."""
        response = self.client.get('/api/v1.0/project/beauty_glamour/'
                                   'desert storm/')
        data = json.loads(response.data)
        self.assertTrue(len(data) == 1)
        self.assertTrue([self.beauty.serialize()] == data)

    def test_get_all_project(self):
        """Test response for get all projects."""
        response = self.client.get('/api/v1.0/project/all/desert storm/')
        data = json.loads(response.data)
        self.assertTrue(len(data) == 3)
        self.assertTrue([self.beauty.serialize(),
                         self.portrait.serialize(),
                         self.fine_art.serialize()] == data)

    def test_wrong_category_name(self):
        """Test response for wrong category name."""
        response = self.client.get('/api/v1.0/project/wrong/desert storm/')
        data = json.loads(response.data)
        self.assertTrue(data["message"] == "The category is not avaiable.")
