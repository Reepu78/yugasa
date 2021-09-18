from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_ChangePasswordPage(BaseTest):

    def test_changePwdButton_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
        assert self.changePasswordPage.is_changePasswordPage_visible() == True

    def test_changePassword_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
        self.changePasswordPage.send_in_oldPwd(TestDataFromExcel.readPassword(self))
        self.changePasswordPage.send_in_newPwd(TestDataFromExcel.NEW_PASSWORD)
        self.changePasswordPage.send_in_confrmPwd(TestDataFromExcel.NEW_PASSWORD)
        TestDataFromExcel.write_in_excel('LoginPage', 2, 2, TestDataFromExcel.NEW_PASSWORD)
        passwordSuccessMessage = self.changePasswordPage.click_submitBTN()
        assert passwordSuccessMessage == TestData.EXPECTED_CHANGE_PASSWORD_SUCCESS_MESSAGE
        self.changePasswordPage.click_signout_btn()
        self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))

    def test_newPassword_validations(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
        if not self.changePasswordPage.check_newPassword_format(TestDataFromExcel.readPassword(self),
                                                             TestDataFromExcel.INV_PWD_LESS_THAN_EIGHT,
                                                             TestDataFromExcel.INV_PWD_LESS_THAN_EIGHT):
            self.changePasswordPage.page_refresh()
            self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
            self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
            if not self.changePasswordPage.check_newPassword_format(TestDataFromExcel.readPassword(self),
                                                             TestDataFromExcel.INV_PWD_NO_SPCLCHAR,
                                                             TestDataFromExcel.INV_PWD_NO_SPCLCHAR):
                self.changePasswordPage.page_refresh()
                self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
                self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
                if not self.changePasswordPage.check_newPassword_format(TestDataFromExcel.readPassword(self),
                                                                        TestDataFromExcel.INV_PWD_NO_LWRCASE,
                                                                        TestDataFromExcel.INV_PWD_NO_LWRCASE):
                    self.changePasswordPage.page_refresh()
                    self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
                    self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
                    if not self.changePasswordPage.check_newPassword_format(TestDataFromExcel.readPassword(self),
                                                                            TestDataFromExcel.INV_PWD_NO_UPPRCASE,
                                                                            TestDataFromExcel.INV_PWD_NO_UPPRCASE):
                        self.changePasswordPage.page_refresh()
                        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
                        self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
                        if not self.changePasswordPage.check_newPassword_format(TestDataFromExcel.readPassword(self),
                                                                                TestDataFromExcel.INV_PWD_NO_NUMBER,
                                                                                TestDataFromExcel.INV_PWD_NO_NUMBER):
                            return True
                        else:
                            return False


    def test_differentPassword_NewAndConfrmPwd(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        self.changePasswordPage = self.editProfilePage.click_changePwdBtn()
        self.changePasswordPage.send_in_oldPwd(TestDataFromExcel.readPassword(self))
        self.changePasswordPage.send_in_newPwd(TestDataFromExcel.NEW_PASSWORD)
        self.changePasswordPage.send_in_confrmPwd(TestDataFromExcel.INVALID_CONFIRM_PASSWORD)
        PasswordChangeAlertText = self.changePasswordPage.click_submitBTN()
        assert PasswordChangeAlertText == TestData.EXPECTED_CHANGE_PASSWORD_ERROR_MESSAGE
