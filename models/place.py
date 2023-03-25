#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
        reviews = relationship('Review', cascade="all, delete",
                               backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') == "fs":
        @property
        def reviews(self):
            from models import storage
            """property that returns a list of city instances"""
            reviewlist = []
            for review in list(storage.all().values()):
                if review.place_id == self.id:
                    reviewlist.append(review)
            return reviewlist

        @property
        def amenities(self):
            from models import storage
            """property that returns a list of city instances"""
            amenitylist = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenitylist.append(amenity)
            return amenitylist

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
