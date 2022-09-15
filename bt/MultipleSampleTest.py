import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep
from btInformation import *

class MultipleSampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        driver = self.driver

        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

        # Register user
        navigate("http://localhost:8080/register.html", driver)
        self.user = fill_random_personnal_infos(driver)
        click_submit("button[type=submit]", driver)

    def test_multiple_sample_submit(self):
        driver = self.driver

        fill_biological_test_with_multiple_samples(self.user, driver)