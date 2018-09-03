"""lesson 5: keys"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')
driver.get('https://www.google.de/')

search_field = driver.find_elements_by_tag_name('input')

for i in search_field:
    if i.is_displayed() and i.is_enabled():
        i.send_keys('google', Keys.BACKSPACE, Keys.ARROW_LEFT, Keys.BACKSPACE, Keys.ENTER)
        break
