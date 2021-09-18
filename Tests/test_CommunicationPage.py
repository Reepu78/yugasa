from Config.TestData import TestData
from Config.config import ConfigData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_CommunicationPage(BaseTest):

    def test_communicationPage_displayed(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.is_headTitle_visble() == True

    def test_download_CSV_Btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.get_downloaded_filePath(ConfigData.COMMUNICATION_DOWNLOAD_CSV_FILE_PATH) == True

    def test_datePicker(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        self.communicationPage.click_calendarDateRange()

    def test_select_all_CheckBox_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        self.communicationPage.click_select_all_checkbox_btn()
        assert self.communicationPage.check_select_all_checkbox_selected() == True

    def test_unselect_all_CheckBox_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        self.communicationPage.click_select_all_checkbox_btn()
        self.communicationPage.click_select_all_checkbox_btn()
        assert self.communicationPage.check_select_all_checkbox_selected() == False

    def test_edit_options_displayed(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.check_edit_elements() == True

    def test_editdata_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.check_update_btn(TestData.EDIT_EMAILID, TestData.EDIT_PHONE) == [
            TestData.EDIT_EMAILID, TestData.EDIT_PHONE]

    def test_delete_Btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        rowsBeforeDeleting = self.communicationPage.count_total_rows()
        nameBeforeDelete = self.communicationPage.get_Name_in_row()
        nameAfterDelete = self.communicationPage.delete_record_get_name()
        rowsAfterDeleting = self.communicationPage.count_total_rows()

        if rowsBeforeDeleting == rowsAfterDeleting:
            assert False
        elif rowsBeforeDeleting != rowsAfterDeleting and nameBeforeDelete == nameAfterDelete:
            assert True
        elif rowsBeforeDeleting != rowsAfterDeleting and nameBeforeDelete != nameAfterDelete:
            assert True

    def test_update_Btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.check_update_btn(TestData.EDIT_EMAILID, TestData.EDIT_PHONE) == [
            TestData.EDIT_EMAILID, TestData.EDIT_PHONE]

    def test_cancel_Btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.click_cancel_btn() == True

    def test_Calendar(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.date_picker_functionality('24 Jul 2020', '28 Aug 2020') == True

    def test_view_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.click_view_button() == True

    def test_status_dropdown_values_correct(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.check_status_dropdown_values() == TestData.STATUS_DROPDOWN_VALUES

    def test_select_status_dropdown_values(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.communicationPage = self.homePage.click_communication_link()
        assert self.communicationPage.select_status_dropdown_values('In Progress') == False





