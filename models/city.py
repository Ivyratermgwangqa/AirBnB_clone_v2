#!/usr/bin/python3
"""This is the class for City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        name: name of the city
        state_id: state id
    """
    __tablename__ = 'cities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
    else:
        name = ""
        state_id = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def state(self):
            """Getter method to return the State object"""
            from models import storage
            state = storage.get('State', self.state_id)
            return state

        @property
        def cities(self):
            """Getter method to return the list of City instances"""
            from models import storage
            cities_list = storage.all('City').values()
            return [city for city in cities_list if city.state_id == self.id]
