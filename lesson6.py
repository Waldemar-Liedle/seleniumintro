"""lesson 6: browser history"""
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')
driver.get('https://www.youtube.de/')
driver.back()
driver.forward()
