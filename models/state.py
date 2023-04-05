#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import shlex
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    storage = getenv("HBNB_TYPE_STORAGE")

    if storage == 'fs':
        @property
        def cities(self):
            """return the cities of the current state"""
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)
