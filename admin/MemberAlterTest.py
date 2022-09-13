import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep

class MemberAlterTest(unittest.TestCase):

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

    def test_update(self):
        driver = self.driver

        # Login as admin
        navigate("http://localhost:8080/profile.html", driver)
        click_by_text("a", "Logout", driver)
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)

        # Update a owner information
        navigate_by_text("a", "Owners", driver)
        navigate_by_text("a.btn-warning", "Update", driver)
        send_keys("#fName2", "___", driver)
        click_submit("button[type=submit]", driver)

        # Check if the information has been updated
        navigate_by_text("a", "Owners", driver)
        self.assertTrue(has_text("td", "___", driver))

    def test_delete(self):
        driver = self.driver

        # Login as admin
        navigate("http://localhost:8080/profile.html", driver)
        click_by_text("a", "Logout", driver)
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)

        # Delete owner
        navigate_by_text("a", "Owners", driver)
        navigate_by_text("a.btn-danger", "Delete", driver)
        click_submit("button[type=submit]", driver)

        # Check if the information has been updated
        navigate_by_text("a", "Owners", driver)
        self.assertFalse(has_text("td", "Delete", driver))
