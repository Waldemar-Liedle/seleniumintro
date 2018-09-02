"""lesson 1"""

from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')
time.sleep(5)
search_field = driver.find_element_by_name('q')
search_field.send_keys('google')
search_field.submit()
time.sleep(5)
driver.quit()