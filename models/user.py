#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    if STORAGE == "db":
      email = Column(String(128), nullable=False)
      password = Column(String(128), nullable=False)
      first_name = Column(String(128),nullable=True)
      last_name = Column(String(128), nullable=True)
      reviews = relationship('Review', backref='user',
                           cascade='delete')
      places = relationship('Place', backref='user',
                          cascade='delete')
      base_model_id = Column(String(60), ForeignKey('base_model.id'))

    else:
      email = ""
      password = ""
      first_name = ""
      last_name = ""
