from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Each class is a separate page of the web app

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def hover_over(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def fetch_element(self,locator):
        # TODO change from visibility other options
        # TODO add try except
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

class HomePage(BasePage):
    """
    Defined methods = actions on the page
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.python.org")

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

class SearchResultsPage(BasePage):

    def is_results_found(self):
        pass
