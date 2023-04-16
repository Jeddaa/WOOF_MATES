from enum import Enum

class Relationship(str, Enum):
    playmate = "Playmate"
    TrainingPartner = "Training Partner"
    BreeddingPartner = "Breedding Partner"
    ServiceDogPartner = "Service Dog Partner"

class Breed(str, Enum):
    Test = "test"

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
