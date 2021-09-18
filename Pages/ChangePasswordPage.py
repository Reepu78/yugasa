from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ChangePasswordPage(BasePage):

    """By Locator"""
    OldPwd = (By.NAME, 'oldPswrd')
    NewPwd = (By.NAME, 'newPswrd')
    ConfrmPwd = (By.NAME, 'cnfrmPswrd')
    SubmitBtn = (By.ID, 'submitBtn')
    ChangePasswordBox = (By.CSS_SELECTOR, 'div.change-pswd-box')
    ChangePasswordAlert = (By.CSS_SELECTOR, 'div.alert')
    SignOut_Btn = (By.XPATH, "(//a[@href='/logOut'])[2]")

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def is_changePasswordPage_visible(self):
        chngPasswordBox_visible = self.is_visible(self.ChangePasswordBox)
        return chngPasswordBox_visible

    def send_in_oldPwd(self, oldpwd):
        Old_pwd = self.do_send_keys(self.OldPwd, oldpwd)
        return Old_pwd

    def send_in_newPwd(self, newPwd):
        self.do_send_keys(self.NewPwd, newPwd)

    def send_in_confrmPwd(self, confrmPwd):
        self.do_send_keys(self.ConfrmPwd, confrmPwd)

    def click_submitBTN(self):
        self.do_click(self.SubmitBtn)
        return self.get_element_text(self.ChangePasswordAlert)

    def click_signout_btn(self):
        self.do_click(self.SignOut_Btn)

    def check_newPassword_format(self, oldpwd, newPwd, confrmPwd):
        self.do_send_keys(self.OldPwd, oldpwd)
        self.do_send_keys(self.NewPwd, newPwd)
        self.do_send_keys(self.ConfrmPwd, confrmPwd)
        self.do_click(self.SubmitBtn)
        return self.is_element_displayed(self.ChangePasswordAlert)

    def page_refresh(self):
        self.driver.refresh()




