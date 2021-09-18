import time

from Pages.LoginPage import LoginPage
from TestData.ExcelLogic import TestDataFromExcel
from Tests.test_base import BaseTest
from Pages.CookiesPage import CookiesPage


class Test_CookiesAcceptPage(BaseTest):

     def test_click_on_accept_button(self):
         self.loginPage = LoginPage(self.driver)
         # self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
         self.cookiesAccept = CookiesPage(self.driver)
         time.sleep(5)
         self.cookiesAccept.click_On_Accept_Btn()

