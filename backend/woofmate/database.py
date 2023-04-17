from sqlalchemy.ext.declarative import declarative_base
from woofmate.schemas.createSchema import ICreateProfile, ICreateUser
from woofmate.schemas.updateSchema import IUpdateProfile
# from woofmate.models import User, Profile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from woofmate.config import settings
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class DB:
#     """DB class"""
#     def find_user_byId(self, user_id:int) -> User:
#         return self.db.query(User).filter(User.id == user_id).first()

#     def find_user_byEmail(db: Session, email:str) -> User:
#         return db.query(User).filter(User.email == email).first()


#     def create_profile(self, user_id: int, profile_data: ICreateProfile) -> Profile:
#         get_user = self.find_user_byId(user_id)
#         new_profile = Profile(user = user_id, **profile_data.dict())
#         get_user.profile.append(new_profile)
#         self.db.add(new_profile)
#         self.db.commit()
#         return new_profile

#     def update_profile(self, user_id: int, profile_id: int, profile_data:IUpdateProfile)-> Profile:
#         try:
#             toUpdateProfile = self.db.query(Profile).filter(Profile.user == user_id, Profile.id == profile_id).first()
#         except NoResultFound:
#             raise ValueError("Could not find profile")
#         profile_data_to_dict = profile_data.dict(exclude_unset=True)
#         for key, value in profile_data_to_dict.items():
#             setattr(toUpdateProfile, key, value)
#         self.db.commit()
#         self.db.refressh(toUpdateProfile)
#         return toUpdateProfile

