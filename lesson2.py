"""lesson 2: unit tests"""
import unittest
from selenium import webdriver


class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\WL\\PycharmProjects\\seleniumintro\\chromedriver')

    def testGoogleSearch(self):
        self.driver.get('https://www.google.de/')
        self.assertIn("Google", self.driver.title)
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('google')
        search_field.submit()
        assert "Es wurden keine mit deiner Suchanfrage" not in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()