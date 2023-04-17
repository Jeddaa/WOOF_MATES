from woofmate.database import Base
from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, DateTime, func
)
from sqlalchemy.orm import relationship
# from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String)
    profile_pic = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    dogProfile_id = relationship(
        'DogProfile', backref='users', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<First name={self.firstName} Last name={self.lastName}>"


class DogProfile(Base):

    # GENDER=(
    #     ('Male','male'),
    #     ('Female','female'),
    # )
    # BREED=(
    #     ('Bulldog', 'bulldog'),
    # )
    # RELATIONSHIP_PREFERENCE=(
    #     ('Playmate','playmate'),
    #     ('Training Partner','training Partner'),
    #     ('Breeding Partner','breeding Partner'),
    # )

    __tablename__ = 'dogprofile'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)

    email = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False, default='Nigeria')
    relationshipPreferences = Column(String, nullable=False)
    pictureURL = Column(
        String, nullable=False, default="https://cloudinary.com/"
    )
    is_active = Column(Boolean, default=True)
    breed = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        """Official string representation of the DogProfile class."""
        return f"<username={self.username} breed={self.breed}>"
