from TestData.ExcelLogic import TestDataFromExcel
from Pages.BasePage import BasePage

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_YourStoryPage(BaseTest):

    def test_your_story_page_displayed(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.yourStoryPage = self.homePage.click_yourstory_link()
        assert self.yourStoryPage.check_your_story_landing_page_visible() == True

    def test_about_textarea_maxlimit(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.yourStoryPage = self.homePage.click_yourstory_link()
        assert self.yourStoryPage.get_max_length_about_textarea() == '1600'

    def test_services_textarea_maxlimit(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.yourStoryPage = self.homePage.click_yourstory_link()
        assert self.yourStoryPage.get_max_length_services_textarea() == '1600'

    def test_terms_textarea_maxlimit(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.yourStoryPage = self.homePage.click_yourstory_link()
        assert self.yourStoryPage.get_max_length_terms_textarea() == '1600'

    def test_contact_textarea_maxlimit(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.yourStoryPage = self.homePage.click_yourstory_link()
        assert self.yourStoryPage.get_max_length_contact_textarea() == '1600'

    def test_other_textarea_maxlimit(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.yourStoryPage = self.homePage.click_yourstory_link()
        assert self.yourStoryPage.get_max_length_other_textarea() == '1600'




