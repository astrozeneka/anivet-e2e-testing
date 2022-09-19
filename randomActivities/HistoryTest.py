import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep
from seleniumrequests import Chrome
import json
from randomActivities import *

class HistoryTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

    def test_history_1(self):
        driver = self.driver
        driver.get("http://localhost:3001/api/v1/fakeTime/set?time=2020-01-01")
        print() # Check it manually

    def test_history_2(self):
        driver = self.driver

        #-----------
        # 2022-01-01
        set_server_time("2022-01-01", driver)
        for i in range(0, 2):
            navigate("http://localhost:8080/register.html", driver)
            fill_random_personnal_infos(driver)
            click_submit("button[type=submit]", driver)

        #-----------
        # 2020-05-05
        set_server_time("2022-05-05", driver)
        for i in range(0, 2):
            navigate("http://localhost:8080/register.html", driver)
            fill_random_personnal_infos(driver)
            click_submit("button[type=submit]", driver)

        #----------
        # 2022-05-06
        # Go to backoffice as admin
        # Login as admin
        driver.get("http://localhost:8080/backoffice.html")
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)

        print() # Check manually


    def test_history_3(self):
        driver = self.driver
        self.users = []
        self.orders = []


        # EACH DAY
        for i in range(1, 4):
            date_str = f"2022-09-{i}"
            set_server_time(date_str, driver)
            self.users = self.users + add_rand_users(2, driver)
            self.orders = self.orders + add_random_orders(3, self.users, driver)

        #-----------
        # September 01
        # Create random users
        print()

    def test_history_4(self):
        driver = self.driver
        self.users = []

        # EACH DAY
        for i in range(1, 4):
            date_str = f"2022-09-{i}"
            set_server_time(date_str, driver)
            self.users = self.users + add_rand_users(1, driver)
            add_random_orders_with_multiple_samples(1, self.users, driver)


        print()
