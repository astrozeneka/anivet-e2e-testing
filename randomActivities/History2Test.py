import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep
import json
from randomActivities import *

class History2Test(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

    def test_history_2_1(self):
        driver = self.driver
        users = add_rand_users(1, driver)
        add_random_orders_with_multiple_samples(3, users, driver)

        print()