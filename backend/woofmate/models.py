from woofmate.database import Base
from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, DateTime, Text, func
)
from sqlalchemy.orm import relationship


class User(Base):
    """
    contains the models and attributes for the user
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String)
    profile_picture = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    dogProfiles = relationship(
        'DogProfile', back_populates='owner', cascade='all, delete-orphan'
    )
    messages_sent = relationship(
        'Message', back_populates='sender', foreign_keys='Message.sender_id'
    )
    messages_received = relationship(
        'Message', back_populates='receiver', foreign_keys='Message.receiver_id'
    )

    def __repr__(self):
        return f"<First name={self.firstName} Last name={self.lastName}>"


class DogProfile(Base):
    """
    Contains the models and attributes for the dog profile 
    """
    __tablename__ = 'dogprofiles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False, default='Nigeria')
    relationship_preferences = Column(String, nullable=False)
    dog_image_1 = Column(String, nullable=False)
    dog_image_2 = Column(String, nullable=False)
    dog_image_3 = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship('User', back_populates='dogProfiles')

    def __repr__(self):
        """Official string representation of the DogProfile class."""
        return f"<name={self.name} breed={self.breed}>"


class Message(Base):
    """
    Contains the models and attributes for the message
    """
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sender = relationship('User', back_populates='messages_sent')
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver = relationship('User', back_populates='messages_received')
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Message from {self.sender.firstName} to {self.receiver.firstName}: {self.content}>"
