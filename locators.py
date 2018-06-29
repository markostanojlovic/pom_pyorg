from selenium.webdriver.common.by import By

# USAGE: For each page create a class and define locators for it

class HomePageLocators:
    """A class with home page locators. All home page locators should come here"""
    TOP_MENU_DOC_BUTTON = (By.ID, "documentation")
    DROPDOWN_PY3_DOC_BUTTON = (By.CSS_SELECTOR, "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)")

class SearchResultsPageLocators: #TODO should be better to use inheritance ? 
    pass
