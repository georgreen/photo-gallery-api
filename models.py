"""Contain All App Models."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """Models, the base model which all other models created inherit from.

    It provide utility methods enabling object to be saved and deleted.
    """

    __abstract__ = True
    uuid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def save(self):
        """Save an instance of a model to the respective table.

        Args:
            self: specify the object to be saved to the table

        Returns:
            True if saving operation was succefull else, False
        """
        try:
            db.session.add(self)
            db.session.commit()
            saved = True
        except Exception as e:
            saved = False
            db.session.rollback()
        return saved

    def delete(self):
        """Delete an instance of a model from the respective table.

        Args:
            self: specify the object to be deleted from the table

        Returns:
            True if delete operation was succefull else. False
        """
        try:
            db.session.delete(self)
            db.session.commit()
            deleted = True
        except Exception:
            deleted = False
            db.session.rollback()
        return deleted

    def serialize(self):
        pass


class Admin(BaseModel):
    __tablename__ = "admins"


class Tag(BaseModel):
    __tablename__ = "tags"
    picture_id = db.Column(db.Integer, db.ForeignKey('pictures.uuid'))


class Picture(BaseModel):
    __tablename__ = "pictures"
    path = db.Column(db.String(100))
    project = db.Column(db.String(50))
    description = db.Column(db.String(256))
    date_created = db.Column(db.String)
    resolution = db.Column(db.String)
    time = db.Column(db.String)
    tags = db.relationship("Tag")

    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'pictures'
    }

    def __init__(self, path, name, project, **meta_data):
        self.path = path
        self.name = name
        self.project = project
        self.tags = meta_data.get('tags', [])


class Fashion(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'fashion'
    }


class BeautyGlamour(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'beauty_glamour'
    }


class Portrait(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'portraits'
    }


class FineArt(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'fine_arts'
    }


class Conceptual(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'conceptuals'
    }


class Composite(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'composites'
    }


class LifeStyle(Picture):
    __mapper_args__ = {
        'polymorphic_identity': 'life_styles'
    }
