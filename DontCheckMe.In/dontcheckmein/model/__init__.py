"""The application's model objects"""
from dontcheckmein.model.meta import Session, Base
from dontcheckmein.model.objects import IgnoreFile


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
