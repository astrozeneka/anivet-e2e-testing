import unittest
import re
from selenium.webdriver.common.by import By
from driver import get_driver
from time import sleep
from utils import *
from registration.personnalInformations import random_personnal_infos
from time import sleep

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")

    def test_user_registration(self):
        driver = self.driver
        driver.get("http://localhost:8080/register.html")
        sleep(0.5)
        self.assertTrue(element_exists("h2", "Personal details", driver))

        user = random_personnal_infos()
        send_keys("#fName1", user['name1'], driver)
        send_keys("#fName2", user['name2'], driver)
        send_keys('#fPhone', user['phone'], driver)
        send_keys('#fEmail', user['email'], driver)
        send_keys('#fCountry', user['country'], driver)
        send_keys('#fAddress', user['address'], driver)
        send_keys('#fChangwat', '**', driver)
        send_keys('#fPostcode', user['postcode'], driver)
        send_keys('#fUsername', user['username'], driver)
        send_keys('#fPassword', user['password'], driver)
        send_keys('#fPasswordCheck', user['passwordCheck'], driver)

        sleep(0.5)
        click("button[type=submit]", driver)

        sleep(0.5)
        self.assertTrue(element_exists("h1", "You have been registered", driver))
        # Should assert
