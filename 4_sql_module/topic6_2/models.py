from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

    address = relationship('Address', back_populates='user')


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email = Column(String(40))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='address')


# Base.metadata.create_all(engine)


