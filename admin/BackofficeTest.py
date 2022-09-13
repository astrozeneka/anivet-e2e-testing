import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep

class BackofficeTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("http://localhost:3001/api/v1/install")
        driver = self.driver

        # Register a Owner
        driver.get("http://localhost:8080/register.html")
        sleep(2)
        self.user = fill_random_personnal_infos(driver, type="owner")
        click("button[type=submit]", driver)
        sleep(0.5)

        # The user registered

    def test_admin_notify_user(self):
        driver = self.driver
        print()

        # Login as admin
        driver.get("http://localhost:8080/backoffice.html")
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click("button[type=submit]", driver)
        sleep(0.5)
        print()

        # Go to owner owner
        click_by_text("a", "Owners", driver)
        sleep(0.5)
        self.assertTrue(element_exists("td", self.user['email'], driver))
        print()

        click_by_text("a", "Message", driver)
        sleep(0.5)
        send_keys("#fTitle", "An example of title", driver)
        send_keys("#fContent", "Hello you from the admin, have a nice day !", driver)
        click("button[type=submit]", driver)
        self.assertTrue(has_text(".alert", "Your message has been sent", driver))
        # Bug à revoir plus tard
        sleep(0.5)

        print()
        click_by_text("a", "Logout", driver)
        driver.get("http://localhost:8080/profile.html")
        sleep(0.5)

        # Login as the new user
        set_select_value("#fType", self.user['type'], driver)
        send_keys("#fUsername", self.user['username'], driver)
        send_keys("#fPassword", self.user['password'], driver)
        click("button[type=submit]", driver)
        sleep(0.5)

        click_by_text("a", "Notifications", driver)
        self.assertTrue(has_text(".alert", "Hello you from the admin", driver))

        print("Done")


