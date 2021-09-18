from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_ConversationalFlowPage(BaseTest):

    def test_conversational_page_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.conversationalFlowPage = self.homePage.click_conversational_flow_link()
        assert self.conversationalFlowPage.get_header_text() == TestData.CONVERSATIONAL_PAGE_HEAD_TEXT

    def test_create_node_dropdown_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.conversationalFlowPage = self.homePage.click_conversational_flow_link()
        assert self.conversationalFlowPage.click_create_node_dropdown_btn() == True

    def test_load_save_btn_clickable(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.conversationalFlowPage = self.homePage.click_conversational_flow_link()
        assert self.conversationalFlowPage.click_load_saved_data_btn() == True

    def test_JSON_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.conversationalFlowPage = self.homePage.click_conversational_flow_link()
        assert self.conversationalFlowPage.click_json_btn() == True

    def test_delete_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.conversationalFlowPage = self.homePage.click_conversational_flow_link()
        assert self.conversationalFlowPage.click_delete_btn() == True
