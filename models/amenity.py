#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base, STORAGE
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary=Place.place_amenity)

    else:
        name = ""
