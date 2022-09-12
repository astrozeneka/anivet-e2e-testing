import unittest
import re
from selenium.webdriver.common.by import By
from driver import get_driver
from time import sleep
from utils import *
from registration.personnalInformations import *
from time import sleep

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")

    # deprecated, don't use anymore
    def test_user_registration(self):
        # The user registered
        # He should be registered
        # The admin receive notification

        driver = self.driver
        driver.get("http://localhost:8080/register.html")
        sleep(0.5)
        self.assertTrue(element_exists("h2", "Personal details", driver))

        # Fill user information
        fill_random_personnal_infos(driver)
        click("button[type=submit]", driver)

        sleep(0.5)
        self.assertTrue(element_exists("h1", "You have been registered", driver))

        # Login as admin
        driver.get("http://localhost:8080/backoffice.html")
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click("button[type=submit]", driver)
        sleep(0.5)

        self.assertTrue(element_exists("h4", "NEW MEMBER", driver))

    def test_user_registration_2(self):
        driver = self.driver
        driver.get("http://localhost:8080/register.html")
        sleep(0.5)
        self.assertTrue(element_exists("h1", "Register as a new user", driver))

        user = fill_random_personnal_infos(driver)
        click("button[type=submit]", driver)
        sleep(0.5)
        self.assertTrue(element_exists("h1", "You have been registered", driver))

        print()


