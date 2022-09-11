import unittest

from selenium.webdriver.common.by import By

from driver import get_driver


class MyTestCase(unittest.TestCase):


    def test_sample_registration(self):
        driver = get_driver()
        driver.get("http://localhost:8080/order.html")
        driver.find_element(By.CSS_SELECTOR, "#fSampleId").send_keys("0001")
        driver.find_element(By.CSS_SELECTOR, "#fAnimal").send_keys("dog")
        driver.find_element(By.CSS_SELECTOR, "#fType").send_keys("blood")
        driver.find_element(By.CSS_SELECTOR, "#fPetId").send_keys("0002")
        driver.find_element(By.CSS_SELECTOR, "#fPetSpecie").send_keys("canine")
        driver.find_element(By.CSS_SELECTOR, "#fImage").send_keys("Hello")
        driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        print()
        # For now manual testing has been used
        # Automatic assertion should be reviewed for later
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
