"""lesson 9: implicit waiting"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedCondition
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.implicitly_wait(5)
driver.get('https://www.google.de/')
element = driver.find_element_by_name('qq')
