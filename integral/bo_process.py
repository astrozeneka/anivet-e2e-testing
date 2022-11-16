
import unittest

from bt.btInformation import fill_biological_test_with_multiple_samples
from randomActivities.random_data import random_reference, random_doc_type, random_receipt_method, random_sample, \
    random_file, random_message
from utils import *
from registration.personnalInformations import *
from time import sleep
import json

class BOProcess(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

        driver = self.driver
        driver.get("http://localhost:8080/login.html")
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)

    def test_add_owner(self):
        driver = self.driver

        driver.get("http://localhost:8080/owner-add.html")
        u = fill_random_personnal_infos_without_type(driver)
        click_submit("button[type=submit]", driver)


    def test_add_owners(self):
        for i in range(0, 10):
            self.test_add_owner()

    def test_add_breeder(self):
        driver = self.driver

        driver.get("http://localhost:8080/breeder-add.html")
        u = fill_random_personnal_infos_without_type(driver)
        click_submit("button[type=submit]", driver)

        print()

    def test_add_breeders(self):
        for i in range(0, 12):
            self.test_add_breeder()

    def test_add_vet(self):
        driver = self.driver
        driver.get("http://localhost:8080/vet-add.html")
        u = fill_random_personnal_infos_without_type(driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_add_vets(self):
        for i in range(0, 3):
            self.test_add_vet()

    def test_add_scientist(self):
        driver = self.driver
        driver.get("http://localhost:8080/scientist-add.html")
        u = fill_random_personnal_infos_without_type_and_address(driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_add_scientists(self):
        for i in range(0, 12):
            self.test_add_scientist()

    def test_add_admin(self):
        driver = self.driver
        driver.get("http://localhost:8080/admin-add.html")
        u = fill_random_personnal_infos_without_type_and_address(driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_add_admins(self):
        for i in range(0, 12):
            self.test_add_admin()

    def test_add_sci_doc(self):
        driver = self.driver
        driver.get("http://localhost:8080/sci-doc-add.html")
        send_keys("#fReference", random_reference(), driver)
        send_keys("#fType", random_doc_type(), driver)
        send_keys("#fFile", "/Users/astrozeneka/Downloads/Billet Ethiopian .pdf", driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_add_sci_docs(self):
        for i in range(0, 16):
            self.test_add_sci_doc()

    def test_add_payment_receipt(self):
        driver = self.driver
        driver.get("http://localhost:8080/payment-receipt-add.html")
        send_keys("#fReference", random_reference(), driver)
        send_keys("#fMethod", random_receipt_method(), driver)
        send_keys("#fFile", "/Users/astrozeneka/Downloads/Billet Ethiopian .pdf", driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_add_payment_receipts(self):
        for i in range(0, 16):
            self.test_add_payment_receipt()

    def test_add_test_sample(self):
        driver = self.driver
        driver.get("http://localhost:8080/test-sample-add.html")
        sample = random_sample()
        send_keys('#fType', sample["type"], driver)
        send_keys('#fAnimal', sample["animal"], driver)
        send_keys('#fPetSpecie', sample["petSpecie"], driver)
        send_keys('#fImage', sample["image"], driver)
        click_submit("button[type=submit]", driver)

    def test_add_test_samples(self):
        for i in range(0, 4):
            self.test_add_test_sample()

    def test_add_test_result(self):
        driver = self.driver
        driver.get("http://localhost:8080/test-result-add.html")
        options = get_selection_option_values("#fSampleId", driver)
        o = {
            "reference": random_reference(),
            "sampleId": random.choice(options[1:]),
            "notes": random_message(),
            "file": random_file()
        }
        send_keys("#fReference", o["reference"], driver)
        set_select_value("#fSampleId", o["sampleId"], driver)
        send_keys("#fNotes", o["notes"], driver)
        send_keys("#fFile", o["file"], driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_add_certification(self):
        # First add samples
        for i in range(0, 5):
            self.test_add_test_sample()
        # After add a test result
        for i in range(0, 5):
            self.test_add_test_result()



