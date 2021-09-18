from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class IntegrationsPage(BasePage):
    """By Locator"""
    Head_Title = (By.CSS_SELECTOR, 'h1.main-title')

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def get_head_title_text(self):
        return self.get_element_text(self.Head_Title)

    
