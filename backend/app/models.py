"""
Module for the database and tables using sqlalchelmy
"""

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, String, Integer, Boolean, Text, LargeBinary,
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
    hashed_password = Column(String(100), nullable=False)
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
    relationshipPreferences = Column(String, nullable=False)
    pictureFilename = Column(String, nullable=False)
    picture = Column(LargeBinary, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship(
        "User", back_populates="dogs", cascade='all, delete-orphan'
    )
