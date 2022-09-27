
import unittest

from bt.btInformation import fill_biological_test_with_multiple_samples
from randomActivities.randomActivities import add_random_orders_with_multiple_samples
from utils import *
from time import sleep
from registration.personnalInformations import *
from randomActivities import *
import json

class RegisterRandomTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

    def test_register(self):
        driver = self.driver
        driver.get("http://localhost:8080/register.html")

        set_select_value("#fType", "breeder", driver)
        u = fill_random_personnal_infos_without_type(driver)
        click_submit("button[type=submit]", driver)

        print()

    def test_register_order(self):
        driver = self.driver


        driver.get("http://localhost:8080/register.html")
        set_select_value("#fType", "breeder", driver)
        u = fill_random_personnal_infos_without_type(driver)
        click_submit("button[type=submit]", driver)


        driver.get("http://localhost:8080/submit-orders.html?lref=sdfsqf")
        # User infos
        send_keys("#fName1", u["name1"], driver)
        send_keys("#fName2", u["name2"], driver)
        send_keys("#fEmail", u["email"], driver)
        fill_biological_test_with_multiple_samples(u, driver)
        click_submit("button[type=submit]", driver)

        print()
