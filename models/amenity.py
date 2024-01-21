#!/usr/bin/python3
"""This is the Amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel, Base):
    """This is the class for Amenity

    Attributes:
        name (str): Amenity name
        place_amenities (relationship): Relationship with Place instances
    """
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)

    # Specify lazy loading for the relationship
    place_amenities = relationship('Place',
                                   secondary='place_amenity',
                                   backref='amenities',
                                   lazy='select',
                                   cascade='delete')
        name = ""
