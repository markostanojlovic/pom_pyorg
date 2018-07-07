import unittest
from selenium import webdriver
from page import HomePage
from locators import HomePageLocators
from locators import LoginPageLocators
from locators import SignupPageLocators
import re

class TestPyOrgHomePage(unittest.TestCase):
    """
    Various example tests for testing python.org
    """
    def setUp(self):
        # TODO make a class that will select browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities={'browserName': 'chrome'})
        self.homepage = HomePage(self.driver)

    def test_TC001_py3_doc_butt_after_doc_hover(self):
        self.homepage.hover_over(self.homepage.fetch_element(HomePageLocators.TOP_MENU_DOC_BUTTON))
        py3docbutton = self.homepage.fetch_element(HomePageLocators.DROPDOWN_PY3_DOC_BUTTON)
        self.assertTrue(py3docbutton.text == "Python 3.x Docs")
        py3docbutton.click()
        self.assertIsNotNone(re.compile('3\..?\..? Documentation').match(self.driver.title))

    def test_TC002_pass_mismatch_message(self):
        self.homepage.click_button(HomePageLocators.BECOME_A_MEMBER_BUTTON)
        self.homepage.click_button(LoginPageLocators.CREATE_NEW_ACCOUNT_BUTTON)
        self.homepage.send_keys(SignupPageLocators.FORM_USER_NAME, "johndoe")
        self.homepage.send_keys(SignupPageLocators.FORM_EMAIL, "johndoe@email.com")
        self.homepage.send_keys(SignupPageLocators.FORM_PASSWORD, "pass123")
        self.homepage.send_keys(SignupPageLocators.FORM_PASSWORD_CONFIRMATION, "pass123456")
        self.homepage.click_button(SignupPageLocators.FORM_SUBMIT_FORM_BUTTON)
        self.assertTrue(self.homepage.fetch_element(SignupPageLocators.PASS_MISMATCH_ERR_MSG).text == "You must type the same password each time.")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
