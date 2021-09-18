from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_IntegrationsPage(BaseTest):

    def test_integration_page_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.integrationPage = self.homePage.click_integration_link()
        assert self.integrationPage.get_head_title_text() == TestData.INTEGRATION_PAGE_HEAD_TEXT



