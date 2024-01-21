#!/usr/bin/python3
"""This is the City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City

    Attributes:
        name (str): City name
        state_id (str): State id (foreign key)
        places (relationship): Relationship with Place instances
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Specify lazy loading for the relationship
    places = relationship('Place', backref='cities', cascade='delete', lazy='select')

    else:
        name = ""
        state_id = ""
