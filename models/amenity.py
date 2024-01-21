#!/usr/bin/python3
"""This is the class for Amenity"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: name of the Amenity
    """
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('PlaceAmenity', back_populates='amenity')
        place_amenities = relationship('PlaceAmenity', back_populates='amenity')
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def place_amenities(self):
            """Getter method to return the list of PlaceAmenity instances"""
            from models import storage
            place_amenities_list = storage.all('PlaceAmenity').values()
            return [place_amenity for place_amenity in place_amenities_list if place_amenity.amenity_id == self.id]
