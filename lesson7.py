"""lesson 7: xpath"""
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')
search_field = driver.find_element_by_xpath("//input[@name='q']")
"""example: //form[@id='?']/div[@id='?']/input[@name='q']"""
"""example: //input[@name='q'][@id='?'][@type='text']"""
search_field.send_keys('google')
search_field.submit()
