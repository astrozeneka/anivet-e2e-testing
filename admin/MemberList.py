import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep


class MemberList(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()

    def test_registerNUsers(self):
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

        for i in range(0, 35):
            navigate("http://localhost:8080/register.html", driver)
            fill_random_personnal_infos(driver)
            click_submit("button[type=submit]", driver)

        print("Done")

    def test_view_all_users(self):
        driver = self.driver


        # Login as admin
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)


        # Go to the owner section
        navigate_by_text("a", "Owners", driver)
        print("Please check manually")