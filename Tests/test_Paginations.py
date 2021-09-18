import time

from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Paginations(BaseTest):


    def test_Fallbacks_pagination_Last_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.click_pagination_Last_button() == True

    def test_Fallbacks_pagination_First_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.click_pagination_first_button() == True

    def test_Fallbacks_pagination_Next_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.click_pagination_next_button() == True

    def test_Fallbacks_pagination_Previous_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.click_pagination_previous_button() == True

    def test_Communications_pagination_Last_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        # time.sleep(2)
        assert self.communicationPage.click_pagination_Last_button() == True

    def test_Communications_pagination_First_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        # time.sleep(2)
        assert self.communicationPage.click_pagination_first_button() == True

    def test_Communications_pagination_Next_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        # time.sleep(2)
        assert self.communicationPage.click_pagination_next_button() == True

    def test_Communications_pagination_Previous_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        # time.sleep(2)
        assert self.communicationPage.click_pagination_previous_button() == True







