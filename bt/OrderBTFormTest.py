import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep
from btInformation import *

class OrderBTFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        driver = self.driver

        navigate("http://localhost:8080/register.html", driver)
        self.user = fill_random_personnal_infos(driver)
        click_submit("button[type=submit]", driver)

        # Login as user
        navigate("http://localhost:8080/profile.html", driver)
        set_select_value("#fType", self.user['type'], driver)
        send_keys("#fUsername", self.user['username'], driver)
        send_keys("#fPassword", self.user['password'], driver)
        click_submit("button[type=submit]", driver)

        navigate("http://localhost:8080/order.html", driver)
        sleep(1)

    def test_normal_filling(self):
        driver = self.driver

        # Not fill anything, just submit
        #click_submit("button[type=submit]", driver)


        #navigate_by_text("button", "Add sample", driver)
        sample1 = fill_biological_test_form(0, driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_submit_without_anything(self):
        driver = self.driver
        click_submit("button[type=submit]", driver)
        print() # Verify by hand

    def test_only_fill_sample_id(self):
        driver = self.driver
        send_keys("#fSampleId0", "0002", driver)
        click_submit("button[type=submit]", driver)
        print() # Verify by hand

    def test_empty_header_field(self):
        driver = self.driver
        clear_input("#fName1", driver)
        clear_input("#fName2", driver)
        clear_input("#fEmail", driver)
        click_submit("button[type=submit]", driver)
        print() # Verify by hand