import time

from Config.TestData import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_ForgotPasswordPage(BaseTest):

    def test_ForgotPasswordLink_works(self):
        self.loginPage = LoginPage(self.driver)
        time.sleep(1)
        self.ForgotPasswordPage = self.loginPage.click_forgotPasswordLink()
        assert self.ForgotPasswordPage.get_headerText() == TestData.FORGOTPASSWORD_HEADER_TEXT





