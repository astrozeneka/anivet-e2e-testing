import random
import unittest

from bt.btInformation import fill_biological_test_with_multiple_samples
from randomActivities.random_data import random_sample, random_reference
from utils import *
from registration.personnalInformations import *
from time import sleep
import json


class RegistrationProcess(unittest.TestCase):

    prefix = "http://localhost:8080"
    prefix = "http://anivet.local"

    def setUp(self):
        self.driver = get_driver()

    def test_registration(self):
        driver = self.driver

        driver.get(f"{self.prefix}/registration-account.html")

        user = random_personnal_infos()
        set_select_value("#fType", user['type'], driver)
        send_keys("#fName1", user['name1'], driver)
        send_keys("#fName2", user['name2'], driver)
        send_keys('#fPhone', user['phone'], driver)
        send_keys('#fEmail', user['email'], driver)
        send_keys('#fCountry', user['country'], driver)
        send_keys('#fAddress', user['address'], driver)
        send_keys('#fChangwat', '**', driver)
        send_keys('#fPostcode', user['postcode'], driver)
        click_submit("button[type=submit]", driver)

        # Accept terms and conditions
        click_submit("button.btn.btn-primary", driver)

        # Register sample
        def add_test_sample():
            sample = random_sample()
            testTypeIds = get_selection_option_values("#fTestTypeId", driver)
            sample["testTypeIds"] = random.choice(testTypeIds[1:])
            set_select_value("#fTestTypeId", sample["testTypeIds"], driver)
            send_keys('#fAnimal', sample["animal"], driver)
            send_keys('#fPetSpecie', sample["petSpecie"], driver)
            send_keys('#fImage', sample["image"], driver)
            click_submit("button[type=submit]", driver)

        # Enter information about test samples
        add_test_sample()
        for i in range(1, 5):
            navigate_by_text("a", "Add", driver)
            add_test_sample()
        navigate_by_text("button", "Confirm", driver)

        # validate invoice and proceed to payment
        navigate_by_text("a", "Proceed", driver)
        methodList = get_selection_option_values("#fMethod", driver)[1:]
        set_select_value("#fMethod", random.choice(methodList), driver)
        send_keys("#fReference", random_reference(), driver)
        send_keys("#fFile", "/Users/astrozeneka/Downloads/Billet Ethiopian .pdf", driver)
        click_submit("button[type=submit]", driver)

        print()