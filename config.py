"""Conatain App configurations."""

class Config(object):
    pass


class Development(Config):
    pass


class Production(Config):
    pass


class Testing(Config):
    pass


class Staging(Config):
    pass


configuration = {
    "Testing" : Testing,
    "Development": Development,
    "Production": Production,
    "Staging": Staging
}