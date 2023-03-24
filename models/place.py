#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'place'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
  

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship('Review', cascade="all, delete", backref='place')
    else:
        @property
        def reviews(self):
            """property that returns a list of city instances"""
            reviewlist = []
            for review in models.storage.all(Review).values():
                if self.id == review.place_id:
                    reviewlist.append(review)
            return reviewlist
        
    if getenv('HBNB_TYPE_STORAGE') == "db":
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)
    else:
        @property
        def amenities(self):
            """property that returns a list of city instances"""
            amenitylist = []
            for amenity in models.storage.all(Amenity).values():
                if self.id == amenity.place_amenity_id:
                    amenitylist.append(amenity)
            return amenitylist
        
    @amenities.setter
    def amenities(self, obj):
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
