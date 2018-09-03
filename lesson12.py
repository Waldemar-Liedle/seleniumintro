"""lesson 12: options"""
from selenium import webdriver
from selenium.webdriver import ActionChains


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


options = webdriver.ChromeOptions()

"""browser window size"""
options.add_argument("start-maximized")

"""path to profiles"""
options.add_argument("user-data-dir=\\path\\to\\profile")

"""path to exetutable"""
options.binary_location = "\\path\\Chrome.exe";

driver = webdriver.Chrome(executeble_path='C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver', chrome_options=options)
driver.get('https://www.google.de/')

ac = ActionChains(driver)
driver.find_element_by_id("gb_70").click()
ac.click_and_hold(driver.find_element_by_class_name("RveJvd"))
ac.pause(2)
ac.move_to_element(driver.find_element_by_name("identifier"))
ac.perform()
