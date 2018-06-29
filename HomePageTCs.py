import unittest
from selenium import webdriver
from page import HomePage
from locators import HomePageLocators
import re

class TestPyOrgHomePage(unittest.TestCase):
    """
    Various example tests for testing python.org
    """
    def setUp(self):
        # TODO make a class that will select browser (with kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_TC001_py3_doc_butt_after_doc_hover(self):
        homepage = HomePage(self.driver)
        homepage.hover_over(homepage.fetch_element(HomePageLocators.TOP_MENU_DOC_BUTTON))
        py3docbutton = homepage.fetch_element(HomePageLocators.DROPDOWN_PY3_DOC_BUTTON)
        self.assertTrue(py3docbutton.text == "Python 3.x Docs")
        py3docbutton.click()
        self.assertIsNotNone(re.compile('3\..?\..? Documentation').match(self.driver.title))

    def test_TC002(self):
        pass

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
