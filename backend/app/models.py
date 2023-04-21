"""
Module for the database and tables using sqlalchelmy
"""

from sqlalchemy.orm import relationship
from sqlalchemy import (
    CheckConstraint, Column, String, Integer, Boolean, Text, JSON,
    ForeignKey, DateTime
)
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    contains the models and table for the dog owner
    which is the user
    """
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)
    profile_picture_url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    dogs = relationship(
        'Dog', back_populates='owner', cascade='all, delete-orphan'
    )


class Dog(Base):
    """
    contains the models and table attributes
    for the dog
    """
    __tablename__ = 'dogs'

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    breed = Column(String(20), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False, default='Nigeria')
    description = Column(Text, nullable=False)
    relationship_preferences = Column(String, nullable=False)
    pictures_url = Column(
    JSON(),
    CheckConstraint(
        "json_array_length(pictures_url) = 3"
    ),
    nullable=False,
    default=[]
)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="dogs")
