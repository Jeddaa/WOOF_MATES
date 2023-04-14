from enum import Enum

class Relationship(str, Enum):
    Playmate = "playmate"
    TrainingPartner = "Training Partner"
    BreeddingPartner = "Breedding Partner"
    ServiceDogPartner = "Service Dog Partner"

class Breed(str, Enum):
    test = "test"

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
