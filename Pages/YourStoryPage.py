from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class YourStoryPage(BasePage):
    """By Locators"""
    YourStory_LandingPage = (By.CSS_SELECTOR, 'div#exTab2')
    About_text_area = (By.CSS_SELECTOR, 'textarea#about')
    Services_text_area = (By.CSS_SELECTOR, 'textarea#services')
    Terms_text_area = (By.CSS_SELECTOR, 'textarea#terms')
    Contact_text_area = (By.CSS_SELECTOR, 'textarea#contact')
    Other_text_area = (By.CSS_SELECTOR, 'textarea#others')
    Train_Your_Story_BTN = (By.CSS_SELECTOR, 'button.uploadstory')
    Success_Message = (By.XPATH, "//div")
    Services_Btn = (By.XPATH, "//h3[contains(text(), 'Services')]")
    Terms_Btn = (By.XPATH, "//h3[contains(text(), 'Terms')]")
    Contact_Btn = (By.XPATH, "//h3[contains(text(), 'Contact')]")
    Other_Btn = (By.XPATH, "//h3[contains(text(), 'Other')]")

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def check_your_story_landing_page_visible(self):
        return self.is_visible(self.YourStory_LandingPage)

    def get_max_length_about_textarea(self):
        return self.get_element_attribute(self.About_text_area, 'maxlength')

    def get_max_length_services_textarea(self):
        self.do_click(self.Services_Btn)
        return self.get_element_attribute(self.Services_text_area, 'maxlength')

    def get_max_length_terms_textarea(self):
        self.do_click(self.Terms_Btn)
        return self.get_element_attribute(self.Terms_text_area, 'maxlength')

    def get_max_length_contact_textarea(self):
        self.do_click(self.Contact_Btn)
        return self.get_element_attribute(self.Contact_text_area, 'maxlength')

    def get_max_length_other_textarea(self):
        self.do_click(self.Other_Btn)
        return self.get_element_attribute(self.Other_text_area, 'maxlength')
