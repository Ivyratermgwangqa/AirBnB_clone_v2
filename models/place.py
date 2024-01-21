#!/usr/bin/python3
"""This is the Place class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table, MetaData
from sqlalchemy.orm import relationship

metadata = Base.metadata

class Place(BaseModel, Base):
    """This is the class for Place

    Attributes:
        city_id (str): City id (foreign key)
        user_id (str): User id (foreign key)
        name (str): Place name
        description (str): Description of the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price for a night's stay
        latitude (float): Latitude
        longitude (float): Longitude
        amenity_ids (relationship): Relationship with Amenity instances
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Specify lazy loading for the relationship
    amenity_ids = relationship('Amenity', secondary='place_amenity', viewonly=False, lazy='select')

    place_amenity = Table('place_amenity', metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            list_review = []
            all_rev = storage.all(Review)
            for value in all_rev.values():
                if value.place_id == self.id:
                    list_review.append(value)
            return list_review

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            list_amenity = []
            all_ameni = storage.all(Amenity)
            for value in all_ameni.values():
                if value.id == self.amenity_ids:
                    list_amenity.append(value)
            return list_amenity

        @amenities.setter
        def amenities(self, value):
            from models import storage
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
