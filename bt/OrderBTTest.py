import unittest
from utils import *
from registration.personnalInformations import *
from time import sleep

class OrderBTTest(unittest.TestCase):

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

    def test_bt_ordering(self):
        driver = self.driver

        # LOGIN AS A USER
        driver.get("http://localhost:8080/profile.html")
        sleep(0.5)
        set_select_value("#fType", self.user['type'], driver)
        send_keys("#fUsername", self.user['username'], driver)
        send_keys("#fPassword", self.user['password'], driver)
        click("button[type=submit]", driver)
        sleep(0.5)
        self.assertTrue(has_text("h2", "My profile", driver))

        # Open the test order page
        navigate("http://localhost:8080/order.html", driver)
        self.assertTrue(has_text("h2", "Order", driver))
        self.assertEqual(input_value("#fEmail", driver), self.user['email'])

        print()

        # Fill Order
        send_keys("#fSampleId", "002", driver)
        send_keys("#fAnimal", "Dog", driver)
        send_keys("#fType", "Blood", driver)
        send_keys("#fPetId", "002", driver)
        send_keys("#fPetSpecie", "Chihuahua", driver)
        send_keys("#fImage", "IMG0004.png", driver)
        click_submit("button[type=submit]", driver)
        sleep(1)

        # Log out and login as admin
        navigate("http://localhost:8080/profile.html", driver)
        click_by_text("a", "Logout", driver)
        navigate("http://localhost:8080/backoffice.html", driver)
        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click_submit("button[type=submit]", driver)

        # Open the order backoffice
        navigate_by_text("a", "Orders", driver)
        assertionText = "From : " + self.user["name1"]
        self.assertTrue(has_text(".alert", assertionText, driver))

