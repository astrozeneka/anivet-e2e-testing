import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep


class BackofficeErrorTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    # Use it Only when the database has been cleared
    def test_registerNUsers(self):
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver
        for i in range(0, 35):
            navigate("http://localhost:8080/register.html", driver)
            fill_random_personnal_infos(driver)
            click_submit("button[type=submit]", driver)
        print("Done")


    def test_auth_emptyInfos(self):
        driver = self.driver
        navigate("http://localhost:8080/backoffice.html", driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_auth_emptyPassword(self):
        driver = self.driver
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        click_submit("button[type=submit]", driver)
        print()
    
    def test_auth_invalidCredentials(self):
        driver = self.driver
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "adfmin", driver)
        click_submit("button[type=submit]", driver)
        print()

    def test_auth_connected(self):
        driver = self.driver
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)
        print()
