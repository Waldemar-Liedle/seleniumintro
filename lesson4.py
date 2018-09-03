"""lesson 4: selecting elements by tag"""
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')

search_field = driver.find_elements_by_tag_name('input')

for i in search_field:
    if i.is_displayed() and i.is_enabled():
        i.send_keys('google')
        i.submit()
        break
