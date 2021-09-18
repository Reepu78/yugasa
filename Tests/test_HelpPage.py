from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_HelpPage(BaseTest):

    def test_help_page_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.helpPage = self.homePage.click_help_link()
        assert self.helpPage.head_title_text() == TestData.HELP_PAGE_HEAD_TEXT

    def test_video_is_playing(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.helpPage = self.homePage.click_help_link()
        assert self.helpPage.click_video_thumb() == True

    def test_contact_us_form_alert(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.helpPage = self.homePage.click_help_link()
        assert self.helpPage.click_contact_us_submit_btn() == TestData.CONTACT_US_ALERT_TEXT





