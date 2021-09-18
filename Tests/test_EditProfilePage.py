from Config.TestData import TestData
from Config.config import ConfigData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_EditProfilePage(BaseTest):

    def test_editProfileButton_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        assert self.editProfilePage.is_editProfilePage_visible() == [True, True, True]

    def test_EmailId_editable(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        flag = self.editProfilePage.isEmailId_enabled()
        assert flag == False

    def test_companyName_editable(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        flag = self.editProfilePage.isCompanyName_enabled()
        assert flag

    def test_changeCompanyName(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        if self.test_companyName_editable():
           self.editProfilePage.change_companyName(TestDataFromExcel.Edit_Company_Name)
        else:
            return False

    def test_newCompName_match_editCompName(self):
        self.test_changeCompanyName()
        ValueAtt_CompName_val = self.editProfilePage.get_CompanyName_ValueAttribute_val('value')
        assert ValueAtt_CompName_val == TestDataFromExcel.Edit_Company_Name

    def test_upload_profile_picture(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.editProfilePage = self.homePage.click_editProfile_LeftMenu()
        self.editProfilePage.upload_file(ConfigData.EDITPROFILE_PROFILE_PIC_PATH) == TestData.EDIT_PROFILE_ALERT_TEXT





