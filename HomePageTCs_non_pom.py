import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re

class TestPyOrgHomePage(unittest.TestCase): # naming convention: Test at the beggining of the class name
    """
    Various example tests for testing python.org
    """
    def setUp(self): # common and will be exec for each test case
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.python.org")

    def test_TC001_py3_doc_butt_after_doc_hover(self): # naming convention: begins with test_
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "documentation")))
        ActionChains(self.driver).move_to_element(element).perform()
        css_selector = "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)"
        py3docbutton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        self.assertTrue(py3docbutton.text == "Python 3.x Docs") #unittest assert method used
        py3docbutton.click()
        self.assertIsNotNone(re.compile('3\..?\..? Documentation').match(self.driver.title))

    def test_TC002_pass_mismatch_message(self):
        css_selector = "#content > div > section > div.psf-widget > p.click-these > a:nth-child(1)"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))).click()
        # redirection to: https://www.python.org/accounts/login/
        css_selector = "#content > div > aside > div > p:nth-child(3) > a"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))).click()
        # redirection to: https://www.python.org/accounts/signup/
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "id_username"))).send_keys("johndoe")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "id_email"))).send_keys("johndoe@email.com")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "id_password1"))).send_keys("pass123")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "id_password2"))).send_keys("pass123456")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#signup_form > button"))).click()
        user_message = "You must type the same password each time."
        usr_msg_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#signup_form > ul > li ")))
        self.assertTrue(usr_msg_element.text == user_message)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
