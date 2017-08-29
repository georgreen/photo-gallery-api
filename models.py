"""Contain All App Models."""
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class BaseModel(db.Model):
    """Models, the base model which all other models created inherit from.

    It provide utility methods enabling object to be saved and deleted,
    it also contain similiar properties in models, which can be inherited by
    subclassing models.
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
        """Map model to a dictionary representation.

        Returns:
            A dict object
        """
        # TODO
        pass


class Admin(BaseModel):
    """Model Admin and admin-roles in app."""

    __tablename__ = "admins"
    _password = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, password, email=""):
        """Initialize admin instance."""
        self.name = name
        self.password = password
        self.email = email

    @property
    def password(self):
        """Read and Write password property."""
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(str(password))

    def authenticate_password(self, password):
        """Validate Admin password."""
        return check_password_hash(self.password, str(password))


class Tag(BaseModel):
    """Models tags that can be associted with a given model instance."""

    __tablename__ = "tags"
    picture_id = db.Column(db.Integer, db.ForeignKey('pictures.uuid'))


class Picture(BaseModel):
    """Base model for pictures, has simmilar properties for all art models."""

    __tablename__ = "pictures"

    path = db.Column(db.String(100))
    project = db.Column(db.String(50))
    description = db.Column(db.String(256))
    resolution = db.Column(db.String)
    date_created = db.Column(db.String)
    day_time = db.Column(db.String)
    tags = db.relationship("Tag")

    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'pictures'
    }

    def __init__(self, path, name, project, **meta):
        """Initilize art models."""
        self.path = path
        self.name = name
        self.project = project
        meta_data = meta.get("meta_data", {})
        self.date_created = meta_data.get('date_created', "")
        self.day_time = meta_data.get('time', "")
        self.resolution = meta_data.get('resolution', "")
        self.description = meta_data.get('description', "")
        self.tags = meta_data.get('tags', [])

    def __repr__(self):
        """Repl representation."""
        return "<{}(name={})>".format(self.__mapper_args__.get(
            'polymorphic_identity'), self.name)


class Fashion(Picture):
    """Model Fashion type in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'fashion'
    }


class BeautyGlamour(Picture):
    """Model BeautyGlamour type in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'beauty_glamour'
    }


class Portrait(Picture):
    """Model Portrait type in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'portraits'
    }


class FineArt(Picture):
    """Model Portrait FineArt in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'fine_arts'
    }


class Conceptual(Picture):
    """Model Conceptual in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'conceptuals'
    }


class Composite(Picture):
    """Model  Composite in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'composites'
    }


class LifeStyle(Picture):
    """Model LifeStyle in pictures."""

    __mapper_args__ = {
        'polymorphic_identity': 'life_styles'
    }
