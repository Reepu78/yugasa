import time

from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_LoginPage(BaseTest):

    def test_RegisterHere_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_registerhere_link_visible()
        assert flag

    def test_logo_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_logo_visible()
        assert flag

    def test_loginpage_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_loginpage_title(TestData.LOGINPAGE_TITLE)
        assert title == TestData.LOGINPAGE_TITLE

    def test_reverse_remember_me_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_remember_me_checkbox()
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        if self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE)  == TestData.HOMEPAGE_TITLE:
            time.sleep(2)
            self.homePage.do_SignOut()
        #remember me checked
        self.loginPage.click_login_button()
        if self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE) == TestData.HOMEPAGE_TITLE:
            self.homePage.do_SignOut()
        time.sleep(3)
        self.loginPage.click_remember_me_checkbox()
        self.loginPage.click_login_button()
        if self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE) == TestData.HOMEPAGE_TITLE:
            self.homePage.do_SignOut()

        self.loginPage.click_login_button()
        if self.homePage.is_leftMenu_DashboardLink_visible():
            assert False
        else:
            assert True


    def test_dologin(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        title = self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE)
        assert title == TestData.HOMEPAGE_TITLE

    def test_dologin_invalidUnamePwd(self):
        self.loginPage = LoginPage(self.driver)
        ActualErrorMsg = self.loginPage.do_login_invalid_Cred(TestDataFromExcel.INVALID_USERNAME,
                                                              TestDataFromExcel.INVALID_PASSWORD)
        assert ActualErrorMsg == TestData.EXPECTED_LOGIN_ERROR_MESSAGE

    def test_dologin_correctUname_incorrectPwd(self):
        self.loginPage = LoginPage(self.driver)
        ActualErrorMsg = self.loginPage.do_login_invalid_Cred(TestDataFromExcel.USERNAME,
                                                              TestDataFromExcel.INVALID_PASSWORD)
        assert ActualErrorMsg == TestData.EXPECTED_LOGIN_ERROR_MESSAGE

    def test_dologin_incorrectUname_correctPwd(self):
        self.loginPage = LoginPage(self.driver)
        ActualErrorMsg = self.loginPage.do_login_invalid_Cred(TestDataFromExcel.INVALID_USERNAME,
                                                              TestDataFromExcel.readPassword(self))
        assert ActualErrorMsg == TestData.EXPECTED_LOGIN_ERROR_MESSAGE


    def test_remember_me_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_remember_me_checkbox()
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        if self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE)  == TestData.HOMEPAGE_TITLE:
            self.homePage.do_SignOut()

        self.loginPage.click_login_button()
        if self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE) == TestData.HOMEPAGE_TITLE:
            assert True
        else:
            assert False









