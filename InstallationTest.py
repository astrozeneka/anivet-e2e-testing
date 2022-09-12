import unittest
import re
from selenium.webdriver.common.by import By
from driver import get_driver
from time import sleep

def element_exists(css_selector, regexp, driver):
    browser = driver
    elts = browser.execute_script(f"return document.querySelectorAll('{css_selector}')")
    cmp = re.compile(regexp)
    for elt in elts:
        if cmp.match(elt.text):
            return True
    return False

def send_keys(css_selector, text, driver):
    driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)

def click(css_selector, driver):
    driver.find_element(By.CSS_SELECTOR, css_selector).click()

class InstallationTest(unittest.TestCase):

    def test_installation_access_to_admin_backoffice(self):
        driver = get_driver()
        driver.get("http://localhost:3001/api/v1/install")

        driver.get("http://localhost:8080/backoffice.html")
        self.assertTrue(element_exists("h1", "Login", driver))

        send_keys("#fUsername", "admin", driver)
        send_keys("#fPassword", "admin", driver)
        click("button[type=submit]", driver)
        sleep(0.5)

        self.assertTrue(element_exists('a', "Logout", driver))

