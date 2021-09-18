import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from selenium.webdriver.support import wait

class CookiesPage(BasePage):


    Cookies_Accept_Button = (By.XPATH,"//*[@id='hs-eu-confirmation-button']")


    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)



    def click_On_Accept_Btn(self):
        self.do_click(self.Cookies_Accept_Button)
