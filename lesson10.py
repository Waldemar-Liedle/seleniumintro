"""lesson 10: explicit waiting with custom condition"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class HasCssClass(object):

    def __init__(self, locator, css):
        self.locator = locator
        self.css = css

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css in element.get_attribute("class"):
            return element
        else:
            return False


driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')
try:
    element = WebDriverWait(driver, 5).until(
        HasCssClass((By.NAME, "q"), "gsfi")
    )
    element.send_keys('google')
    time.sleep(5)
finally:
    driver.quit()
