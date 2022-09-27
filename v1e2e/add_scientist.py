
import unittest
from utils import *
from time import sleep
from registration.personnalInformations import *
from randomActivities import *
import json

class AddScientistTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

        #----------
        # 2022-05-06
        # Go to backoffice as admin
        # Login as admin
        driver.get("http://localhost:8080/login.html")
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)


    def test_case_1(self):
        driver = self.driver

        navigate_by_text("a", "Scientists", driver)
        navigate_by_text("a", "Add", driver)

        # Add random scientist
        u = fill_random_personnal_infos_without_type(driver)
        click_submit("button[type=submit]", driver)

        print()
