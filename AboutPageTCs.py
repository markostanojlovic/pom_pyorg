import unittest
from selenium import webdriver
from page import AboutPage
from locators import AboutPageLocators

class TestPyOrgAboutPage(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.aboutpage = AboutPage(self.driver)

    def test_TC003_verify_upcoming_events_section_present(self):
        self.assertTrue(self.aboutpage.fetch_element(AboutPageLocators.UPCOMING_EVENTS_SECTION).text == "Upcoming Events")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
