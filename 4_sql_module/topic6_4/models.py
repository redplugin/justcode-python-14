from sqlalchemy import Column, Integer, String, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import relationship

from database import Base, engine


# UNIQUE, NOT NULL
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False, index=True)
    name = Column(String(30))
    surname = Column(String(30))

    posts = relationship('Post', uselist=True, cascade='all,delete', back_populates='author')


# content text CHECK length(content) < 50
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)

    content = Column(Text, CheckConstraint('LENGTH(content) < 50'))

    author = relationship('User', uselist=False, cascade='all,delete', back_populates='posts')


Base.metadata.create_all(engine)


