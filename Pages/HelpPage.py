import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class HelpPage(BasePage):

    """By Locator"""
    Head_Title = (By.CSS_SELECTOR, "h1.main-title2")
    Video_Thumb = (By.XPATH, "(//div[@class = 'video-thumb'])[1]")
    Video_Play = (By.CSS_SELECTOR, 'video#intro')
    ContactUs_Title = (By.NAME, 'title')
    ContactUs_Message = (By.NAME, 'query')
    ContactUs_Send_Btn = (By.XPATH, "//button[@type= 'submit']")



    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def head_title_text(self):
        return self.get_element_text(self.Head_Title)

    def click_video_thumb(self):
        self.do_click(self.Video_Thumb)
        return self.is_element_displayed(self.Video_Play)

    def click_contact_us_submit_btn(self):
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        time.sleep(1)
        self.do_send_keys(self.ContactUs_Title, 'Test')
        self.do_send_keys(self.ContactUs_Message, 'Test')
        ActionChains(self.driver).move_to_element(self.get_element(self.ContactUs_Send_Btn)).click().perform()
        time.sleep(1)
        return self.get_alert_text()





