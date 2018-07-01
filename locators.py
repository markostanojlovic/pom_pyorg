from selenium.webdriver.common.by import By

# USAGE: For each page create a class and define locators for it

class HomePageLocators:
    """A class with home page locators. All home page locators should come here"""
    TOP_MENU_DOC_BUTTON = (By.ID, "documentation")
    DROPDOWN_PY3_DOC_BUTTON = (By.CSS_SELECTOR, "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)")
    BECOME_A_MEMBER_BUTTON = (By.CSS_SELECTOR, "#content > div > section > div.psf-widget > p.click-these > a:nth-child(1)")

class LoginPageLocators: #TODO should be better to use inheritance ?
    """A class with login page locators. All login page locators should come here"""
    CREATE_NEW_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#content > div > aside > div > p:nth-child(3) > a")

class SignupPageLocators:
    """A class with signup page locators. All signup page locators should come here"""
    FORM_USER_NAME = (By.ID, "id_username")
    FORM_EMAIL = (By.ID, "id_email")
    FORM_PASSWORD = (By.ID, "id_password1")
    FORM_PASSWORD_CONFIRMATION = (By.ID, "id_password2")
    FORM_SUBMIT_FORM_BUTTON = (By.CSS_SELECTOR, "#signup_form > button")
    PASS_MISMATCH_ERR_MSG = (By.CSS_SELECTOR, "#signup_form > ul > li ")

class AboutPageLocators:
    """A class with about page locators. All about page locators should come here"""
    UPCOMING_EVENTS_SECTION = (By.CSS_SELECTOR, "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > h2")
