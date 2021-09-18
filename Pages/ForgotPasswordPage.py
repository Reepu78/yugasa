from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ForgotPasswordPage(BasePage):
    """By Locators"""
    Header = (By.CSS_SELECTOR, "span.head-text")
    EmailId = (By.NAME, "email")
    SendBtn = (By.ID, "sendBtn")

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def get_headerText(self):
        headerText = self.get_element_text(self.Header)
        return headerText
