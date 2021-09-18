import pickle
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import ConfigData
from Pages.BasePage import BasePage
from Pages.ForgotPasswordPage import ForgotPasswordPage
from Pages.HomePage import HomePage
from Pages.RegistrationPage import RegistrationPage


class LoginPage(BasePage):
    """By Locators"""
    Username = (By.ID, "username")
    Password = (By.ID, "password")
    LoginButton = (By.ID, "submitBtn")
    RegisterHere_LINK = (By.LINK_TEXT, "Register Here")
    Logo = (By.XPATH, "//a[@href = 'https://helloyubo.com/']")
    ForgotPassword_Link = (By.LINK_TEXT, "Forgot Password")
    LoginError_Msg = (By.CSS_SELECTOR, 'div.alert')
    Remember_Me_CheckBox = (By.CSS_SELECTOR, 'input#exampleCheck1')
    Cookie_Accept = (By.LINK_TEXT, 'Accept')

    """Constructor of the Page Class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.BASE_URL)

    """Page Actions"""

    def get_loginpage_title(self, title):
        return self.get_title(title)

    def is_logo_visible(self):
        return self.is_visible(self.Logo)

    def is_registerhere_link_visible(self):
        return self.is_visible(self.RegisterHere_LINK)

    def is_forgotPasswordlink_visible(self):
        return self.is_visible(self.ForgotPassword_Link)

    def click_forgotPasswordLink(self):
        self.do_click(self.ForgotPassword_Link)
        return ForgotPasswordPage(self.driver)

    def do_login(self, username, password):
        try:
            if WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.Cookie_Accept)):
                self.do_click(self.Cookie_Accept)
                self.do_send_keys(self.Username, username)
                self.do_send_keys(self.Password, password)
                self.do_click(self.LoginButton)
                return HomePage(self.driver)

        except TimeoutException:
            self.do_send_keys(self.Username, username)
            self.do_send_keys(self.Password, password)
            self.do_click(self.LoginButton)
            return HomePage(self.driver)

    def accept_cookies(self):
        self.do_click(self.Cookie_Accept)

    def do_login_invalid_Cred(self, username, password):
        self.do_send_keys(self.Username, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.LoginButton)
        return self.get_element_text(self.LoginError_Msg)

    def do_login_correctUname_incorrectPWD(self, username, password):
        self.do_send_keys(self.Username, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.LoginButton)
        return self.get_element_text(self.LoginError_Msg)

    def click_RegisterHere_link(self):
        self.do_click(self.RegisterHere_LINK)
        return RegistrationPage(self.driver)

    def click_remember_me_checkbox(self):
        self.do_click(self.Remember_Me_CheckBox)

    def click_login_button(self):
        self.do_click(self.LoginButton)
