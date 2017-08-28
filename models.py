"""Contain All App Models."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    uuid = db.Column(db.Integer, primary_key=True)

    def save(self):
        pass

    def delete(self):
        pass

    def serialize(self):
        pass


class Admin(BaseModel):
    __tablename__ = "admins"
    pass


class ArtWork(BaseModel):
    __abstract__ = True
    pass


class Fashion(ArtWork):
    __tablename__ = "fashion"
    pass


class BeautyGlamour(ArtWork):
    __tablename__ = "beauty"
    pass


class Portaits(ArtWork):
    __tablename__ = "potraits"
    pass


class FineArt(ArtWork):
    __tablename__ = "fineart"
    pass


class Conceptual(ArtWork):
    __tablename__ = "conceptual"
    pass


class Composites(ArtWork):
    __tablename__ = "composites"
    pass


class LifeStyle(ArtWork):
    __tablename__ = "lifestyle"
    pass
