#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column("id", String(60), primary_key=True,
                nullable=False)
    created_at = Column("created_at", DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column("updated_at", DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if args:
            raise TypeError("BaseModel() takes no positional arguments")
        form = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            if kwargs.get('id') is None:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.datetime.now()
                self.updated_at = datetime.datetime.now()
            else:
                for k, v in kwargs.items():
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.datetime.strptime(v, form)
                    if k != '__class__':
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
