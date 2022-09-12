
from selenium.webdriver.common.by import By
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver():
    s = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=s, options=options)
    return driver

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
    driver.execute_script(f"""
    let elt = document.querySelector('{css_selector}')
    elt.click()
    """)
    # driver.find_element(By.CSS_SELECTOR, css_selector).click()
