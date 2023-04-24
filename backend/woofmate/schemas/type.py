from enum import Enum


class Relationship(str, Enum):
    playmate = "Playmate"
    TrainingPartner = "Training Partner"
    BreeddingPartner = "Breedding Partner"
    ServiceDogPartner = "Service Dog Partner"
    Companionship = "Companionship"


class Breed(str, Enum):
    Dalmatian = "Dalmatian"
    GermanShepherd = "German Shepherd"
    Poodle = "Poodle"
    LabradorRetriever = "Labrador Retriever"
    GoldenRetriever = "Golden Retriever"
    Rottweiler = "Rottweiler"
    Beagle = "Beagle"
    FrenchBulldog = "French Bulldog"
    Maltipoo = "Maltipoo"
    ShihTzu = "Shih Tzu"
    YorkshireTerrier = "Yorkshire Terrier"
    Chihuahua = "Chihuahua"
    Pomeranian = "Pomeranian"
    Boxer = "Boxer"
    Bulldog = "Bulldog"
    EuropeanBulldog = "European Bulldog"
    EuropeanDoberman = "European Doberman"
    GreatDane = "Great Dane"
    Husky = "Husky"
    Maltese = "Maltese"
    CokerSpaniel = "Coker Spaniel"
    EnglishBulldog = "English Bulldog"
    StandardPoodle = "Standard Poodle"
    MiniaturePoodle = "Miniature Poodle"
    BassettHound = "Bassett Hound"
    Samoyed = "Samoyed"
    MiniaturePinscher = "Miniature Pinscher"
    EnglishCockerSpaniel = "English Cocker Spaniel"
    PembrokeWelshCorgi = "Pembroke Welsh Corgi"
    CaneCorso = "Cane Corso"
    Dachshund = "Dachshund"
    BorderCollie = "Border Collie"
    AustralianShepherd = "Australian Shepherd"
    Alsatian = "Alsatian"
    ShibaInu = "Shiba Inu"
    Bullmastiff = "Bullmastiff"
    SiberianHusky = "Siberian Husky"
    EnglishMastiff = "English Mastiff"
    BullTerrier = "Bull Terrier"
    DobermanPinscher = "Doberman Pinscher"
    AmericanPitBull = "American Pit Bull "
    RhodesianRidgeback = "Rhodesian Ridgeback"





class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
