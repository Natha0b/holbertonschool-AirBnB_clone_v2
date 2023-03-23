#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class DBStorage:
    """Private attributes"""
    __engine = None
    __session = None

    def __init__(self):
        """Public insstance methods with enviroment varibles"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """something"""
        classdict = {}
        if cls is None:
            cls = [State, City, User, Place, Review, Amenity]
        else:
            cls = [cls]
        for classes in cls:
            for result in self.__session.query(classes).all():
                key = "{}.{}".format(type(result).__name__, result.id)
                classdict[key] = result
        return classdict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Create alltables in the database"""
        Base.metadata.create_all(self.__engine)
        Session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(Session_factory)
        self.__session = Session()
