import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep

class BackofficeUpdateMemberErrorTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        driver = self.driver

        # Login as admin
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)

        # Go to the owner section
        navigate_by_text("a", "Owners", driver)
        print("Please check manually")

        # Update a owner information
        navigate_by_text("a", "Owners", driver)
        navigate_by_text("a.btn-warning", "Update", driver)



    # Use it to populate the database
    def test_registerNUsers(self):
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver
        for i in range(0, 35):
            navigate("http://localhost:8080/register.html", driver)
            fill_random_personnal_infos(driver)
            click_submit("button[type=submit]", driver)
        print("Done")

    def test_empty_all(self):
        driver = self.driver

        sleep(0.5)
        clear_input("#fName1", driver)
        clear_input("#fName2", driver)
        clear_input("#fPhone", driver)
        clear_input("#fEmail", driver)
        click_submit("button[type=submit]", driver)
        print() # Check manualy

    def test_empty_really(self):
        driver = self.driver
        sleep(0.5)
        clear_input("#fName1", driver)
        clear_input("#fName2", driver)
        clear_input("#fPhone", driver)
        clear_input("#fEmail", driver)
        clear_input("#fAddress1", driver)
        clear_input("#fCountry", driver)
        clear_input("#fChangwat", driver)
        clear_input("#fPostcode", driver)
        clear_input("#fUsername", driver)
        clear_input("#fWebsite", driver)
        click_submit("button[type=submit]", driver)
        print() # Check manually

    # Test update
    def test_update_country(self):
        driver = self.driver
        sleep(0.5)
        clear_input("#fCountry", driver)
        send_keys("#fCountry", "China", driver)
        click_submit("button[type=submit]", driver)
        print() # Check manually

    def test_empty_username(self):
        driver = self.driver
        sleep(0.5)
        clear_input("#fUsername", driver)
        click_submit("button[type=submit]", driver)
        print() # Check manually