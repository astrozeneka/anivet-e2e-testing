import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep


class BackofficePopulate(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        driver = self.driver

        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

    def test_populate(self):
        driver = self.driver

        # Fill with n=8 users
        users = []
        for i in range(0, 8):
            navigate("http://localhost:8080/register.html", driver)
            fill_random_personnal_infos(driver)
            click_submit("button[type=submit]", driver)
        print("Done")

        # Each user order 0, 1, 2, 3 or 4 test
        test = []