
import unittest

from bt.btInformation import fill_biological_test_with_multiple_samples
from utils import *
from registration.personnalInformations import *
from time import sleep
import json

class RegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def test_registration(self):
        driver = self.driver

        driver.get("http://anivet.local/register.html")

        # FILL INFORMATION ON THE WEBSITE
        u = fill_random_personnal_infos(driver)
        # set_select_value("#fType", "breeder", driver)
        click_submit("button[type=submit]", driver)

        # USER ACCEPT THE TERMS AND CONDITIONS
        navigate_by_text("button", "Accept", driver)
        sleep(2.2) # Wait two seconds

        # FILL ORDERS
        send_keys("#fName1", u["name1"], driver)
        send_keys("#fName2", u["name2"], driver)
        send_keys("#fEmail", u["email"], driver)
        fill_biological_test_with_multiple_samples(u, driver)
        click_submit("button[type=submit]", driver)

        # ACCEPT AND PROCEED TO PAYMENT
        navigate_by_text("button", "Proceed to payment", driver)

        # FILL PAYMENT INFORMATIONS
        send_keys("#fReference", "R"+str(random.randint(0, 2000)), driver)
        send_keys("#fMethod", "Thai QR", driver)
        send_keys("#fFile", "/Users/astrozeneka/Downloads/Billet Ethiopian .pdf", driver)
        navigate_by_text("button", "Submit", driver)

        print()

    def test_registration_x15(self):
        for i in range(0, 3):
            self.test_registration()

        print()