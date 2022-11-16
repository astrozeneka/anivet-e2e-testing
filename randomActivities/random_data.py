import random
import lorem
def random_reference():
    o = random.choice("ABCDEFGHIJKLMNOPQRST")
    o+= random.choice("0123456789")
    o+= random.choice("0123456789")
    o+= random.choice("0123456789")
    o+= random.choice("0123456789")
    return o

def random_doc_type():
    arr = ["certification", "pcr", "receipt", "mail"]
    return random.choice(arr)

def random_receipt_method():
    arr = ["QR", "Cash", "Bank", "Crypto"]
    return random.choice(arr)

def random_sample():
    animal_list = ["Dog", "Cat", "Bird", "Snake"]
    animal_specie_list = {
        "Dog": ["German shepherd", "Doberman", "Labrador", "Thai bangkaew", "Dalmatian"],
        "Cat": ["Ringtail", "Asian", "Balinese", "British shorthair", "Burmanese", "Egyptian Mau"],
        "Bird": ["Chicken", "Pigeon", "Macao", "Common parrots", "Duck"],
        "Snake": ["Python", "Anaconda", "Boa"],
        "Lemur": ["Ring-tailed", "Greater bamboo", "Brown Mouse"]
    }
    type_list = ["Blood", "Skin", "Saliva"]
    animal = random.choice(animal_list)
    return {
        'type': random.choice(type_list),
        'animal': animal,
        'petSpecie': random.choice(animal_specie_list[animal]),
        'image': '/Users/astrozeneka/Downloads/argouml-0.35.1/icon/ArgoIcon512x512.png'
    }

def random_message():
    return lorem.sentence()

from glob import glob
def random_file():
    file_list = glob("/Users/astrozeneka/Documents/codeur.com/en-cours/Projet-InTEnSeA/src/assets/images/Test2/*")
    return random.choice(file_list)