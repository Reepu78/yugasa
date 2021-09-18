from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_HomePage(BaseTest):

    def test_homepage_title(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        title = self.homePage.get_homepage_title(TestData.HOMEPAGE_TITLE)
        assert title == TestData.HOMEPAGE_TITLE

    def test_HomePageLogo_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        flag = self.homePage.is_homePageLogo_visible()
        assert flag

    def test_leftMenu_DashboardLink_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        flag = self.homePage.is_leftMenu_DashboardLink_visible()
        assert flag

    def test_leftMenu_SignOutLink_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        flag = self.homePage.is_leftMenu_SignOutLink_visible()
        assert flag

    def test_leftMenu_SignOut(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.homePage.do_SignOut()
        assert self.loginPage.get_loginpage_title(TestData.LOGINPAGE_TITLE) == TestData.LOGINPAGE_TITLE

    def test_check_broken_links(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.get_all_Links_Status_Code() != '404'

    def test_side_menu_links_position(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.check_all_links_side_menu_visible() == TestData.LINK_NAMES

    def test_link_notOpen_newTab(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.click_all_Links() == True

    def test_all_dashboard_elements_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.is_Dashboard_Elements_visible() == True

    def test_ProgressChart_filter(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.get_Chart_Filter_dropDown_Options() == TestData.Expected_Chart_Filters_Options

    def test_datePicker_clickable(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.click_Calendar_Range() == True

    def test_today_date_displayed(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        assert self.homePage.get_today_date() == self.homePage.get_end_date_calendar()

    def test_communication_data_correct(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        Convo_Displayed = self.homePage.get_No_of_Conversation_dislayed()
        self.cp = self.homePage.click_communication_link()
        assert self.cp.get_total_customer_chats() == int(Convo_Displayed)

    def test_no_of_visitor_data_correct(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        visitor_Displayed = self.homePage.get_No_of_Visitors_displayed()
        self.cp = self.homePage.click_communication_link()
        assert self.cp.count_total_rows() == int(visitor_Displayed)

    def test_no_of_total_leads_correct(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        totalLeads_Displayed = self.homePage.get_No_of_Total_Leads_displayed()
        self.cp = self.homePage.click_communication_link()
        self.cp.select_Leads_Dropdown()
        assert self.cp.count_total_rows() == int(totalLeads_Displayed)

    def test_unhandled_fallbacks_data_correct(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        unhandled_fallbacks_Displayed = self.homePage.get_No_of_unhandled_fallbacks()
        self.fallbacksPage =  self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.count_total_rows() == int(unhandled_fallbacks_Displayed)



