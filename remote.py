import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestPyOrgAboutPage(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.python.org/about/")

    def test_TC003_verify_upcoming_events_section_present(self):
        css_locator = "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > h2"
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_locator)))
        self.assertTrue(element.text == "Upcoming Events")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
