"""Module contain tests for models."""

try:
    from models import (Fashion, Picture, Tag, BeautyGlamour, Portrait,
                        FineArt, Conceptual, Composite, LifeStyle, Admin)
except ImportError:
    from photo_app.models import (Fashion, Picture, Tag, BeautyGlamour,
                                  Portrait, FineArt, Conceptual, Composite,
                                  LifeStyle, Admin)

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
                              "tags": [self.tag]
                              })
        self.assertTrue(fashion.save())
        new_fashion_instance = Picture.query.filter_by(
            type="fashion").filter_by(name="newfashionitem").first()
        self.assertTrue(new_fashion_instance == fashion)
        self.assertTrue(new_fashion_instance.description == "All winds go!")
        self.assertTrue(new_fashion_instance.tags)

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

    def test_serialize_model(self):
        """Test models can be serilized."""
        self.assertTrue(self.fashion.save())
        serilize_model = self.fashion.serialize()
        self.assertTrue(serilize_model)
        self.assertTrue(serilize_model['name'] == "test-fashion-instance")


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
        """Test BeautyGlamour instance can be created."""
        beauty = BeautyGlamour(path="/img/beuty.jpeg",
                               name="newbeautyitem",
                               project="desert storm",
                               meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags": [self.tag]
                                  })
        self.assertTrue(beauty.save())
        new_beauty_instance = Picture.query.filter_by(
            type="beauty_glamour").filter_by(name="newbeautyitem").first()
        self.assertTrue(new_beauty_instance == beauty)


class TestPortrait(BaseTestCase):
    """Test Portait model."""

    def test_create_Portrait_object(self):
        """Test Portrait instance can be created."""
        portrait = Portrait(path="/img/image.jpeg",
                            name="newimageitem",
                            project="desert storm 2",
                            meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags": [self.tag]
                                  })
        self.assertTrue(portrait.save())
        new_potrait_instance = Picture.query.filter_by(
            type="portraits").filter_by(name="newimageitem").first()
        self.assertTrue(new_potrait_instance == portrait)


class TestFineArt(BaseTestCase):
    """Test FineArt model."""

    def test_create_FineArt_object(self):
        """Test FineArt instance can be created."""
        fine_art = FineArt(path="/img/image.jpeg",
                           name="newimageitem",
                           project="desert storm 2",
                           meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags": [self.tag]
                                  })
        self.assertTrue(fine_art.save())
        new_fine_art_instance = Picture.query.filter_by(
            type="fine_arts").filter_by(name="newimageitem").first()
        self.assertTrue(new_fine_art_instance == fine_art)


class TestConceptual(BaseTestCase):
    """Test Conceptual model."""

    def test_create_Conceptual_object(self):
        """Test Conceptual instance can be created."""
        conceptual = Conceptual(path="/img/image.jpeg",
                                name="newimageitem",
                                project="desert storm 2",
                                meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags": [self.tag]
                                  })
        self.assertTrue(conceptual.save())
        new_conceptual_instance = Picture.query.filter_by(
            type="conceptuals").filter_by(name="newimageitem").first()
        self.assertTrue(new_conceptual_instance == conceptual)


class TestComposite(BaseTestCase):
    """Test Composite model."""

    def test_create_Conceptual_object(self):
        """Test Composite instance can be created."""
        composite = Composite(path="/img/image.jpeg",
                              name="newimageitem",
                              project="desert storm 2",
                              meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags": [self.tag]
                                  })
        self.assertTrue(composite.save())
        new_composite_instance = Picture.query.filter_by(
            type="composites").filter_by(name="newimageitem").first()
        self.assertTrue(new_composite_instance == composite)


class TestLifeStyle(BaseTestCase):
    """Test LifeStyle model."""

    def test_create_LifeStyle_object(self):
        """Test LifeStyle instance can be created."""
        life_style = LifeStyle(path="/img/image.jpeg",
                               name="newimageitem",
                               project="desert storm 2",
                               meta_data={
                                  "description": "All winds go!",
                                  "date_created": "12/01/1997",
                                  "resolution": "720X1800",
                                  "time": "noon",
                                  "tags": [self.tag]
                                  })
        self.assertTrue(life_style.save())
        new_life_style_instance = Picture.query.filter_by(
            type="life_styles").filter_by(name="newimageitem").first()
        self.assertTrue(new_life_style_instance == life_style)


class TestAdmin(BaseTestCase):
    """Test Admin model."""

    def test_create_admin_instance(self):
        """Test create_admin instance."""
        admin = Admin(name="test Admin", password="hardtogeuss")
        self.assertTrue(admin.save())
        new_admin_instance = Admin.query.filter_by(name="test Admin").first()
        self.assertTrue(new_admin_instance == admin)

    def test_aadmin_password(self):
        """Test Admin password."""
        self.assertTrue(self.admin.save())
        self.admin.password = "newhardpassword"
        self.admin.save()
        self.assertTrue(self.admin.password != "newhardpassword")
        self.assertTrue(self.admin.authenticate_password("newhardpassword"))
