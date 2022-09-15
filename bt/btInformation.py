import random
from time import sleep
from utils import *

animal_list = ["Dog", "Cat", "Bird", "Snake", "Lemur"]
animal_specie_list = {
    "Dog": ["German shepherd", "Doberman", "Labrador", "Thai bangkaew", "Dalmatian"],
    "Cat": ["Ringtail", "Asian", "Balinese", "British shorthair", "Burmanese", "Egyptian Mau"],
    "Bird": ["Chicken", "Pigeon", "Macao", "Common parrots", "Duck"],
    "Snake": ["Python", "Anaconda", "Boa"],
    "Lemur": ["Ring-tailed", "Greater bamboo", "Brown Mouse"]
}
type_list = ["Blood", "Skin", "Saliva"]

def random_biological_test():
    animal = random.choice(animal_list)
    return {
        'sampleId': str(random.randint(1, 9999)),
        'animal': animal,
        'type': random.choice(type_list),
        'petId': str(random.randint(1, 9999)),
        'petSpecie': random.choice(animal_specie_list[animal]),
        'image': ''
    }

def fill_biological_test_form(index, driver):
    sample = random_biological_test()
    index = str(index)
    send_keys("#fSampleId" + index, sample["sampleId"], driver)
    send_keys("#fAnimal" + index, sample["animal"], driver)
    send_keys("#fType" + index, sample["type"], driver)
    send_keys("#fPetId" + index, sample["petId"], driver)
    send_keys("#fPetSpecie" + index, sample["petSpecie"], driver)
    send_keys("#fImage" + index, sample["image"], driver)
    sleep(0.5)
    return sample

def fill_biological_test_with_multiple_samples(user, driver):

    sample_len = random.randint(1, 8)
    for i in range(0, sample_len-1):
        fill_biological_test_form(i, driver)
        navigate_by_text("button", "Add sample", driver)
    fill_biological_test_form(sample_len-1, driver)
