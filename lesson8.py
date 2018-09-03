"""lesson 8: explicit waiting"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedCondition
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')
try:
    element = WebDriverWait(driver, 5).until(
        ExpectedCondition.presence_of_element_located((By.NAME, "q"))
    )
    element.send_keys('google')
    time.sleep(5)
finally:
    driver.quit()
