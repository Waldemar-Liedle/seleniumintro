"""lesson 3: selecting elements by class"""
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')

search_field = driver.find_elements_by_class_name('gsfi')
for i in search_field:
    if i.tag_name == "input":
        i.send_keys('google')
        i.submit()
        break
