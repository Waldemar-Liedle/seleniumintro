"""lesson 10: action chain (only on one page)"""
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')

ac = ActionChains(driver)
driver.find_element_by_id("gb_70").click()
ac.click_and_hold(driver.find_element_by_class_name("RveJvd"))
ac.pause(2)
ac.move_to_element(driver.find_element_by_name("identifier"))
ac.perform()
