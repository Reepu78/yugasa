import time

from Config.TestData import TestData
from Config.config import ConfigData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.CreateIntentPage import CreateIntentPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_FallbacksPage(BaseTest):

    def test_Ignore_Btn_PopUp_Ok_Btn_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        self.fallbacksPage.click_ignoreBtn()
        TestDataFromExcel.readPassword(self)
        assert self.fallbacksPage.get_Ignore_Btn_PopUp_Title() == TestData.IGNORE_BTN_POPUP_TITLE
        assert self.fallbacksPage.get_Ignore_Btn_PopUp_MainText() == TestData.IGNORE_BTN_POPUP_HEADER_TEXT
        assert self.fallbacksPage.is_Ignore_Btn_PopUp_CancelBtn_visible() == True
        assert self.fallbacksPage.is_Ignore_Btn_PopUp_OkBtn_visible() == True

    def test_Ignore_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.check_delete_button_functionality() == True

    def test_row_count_update_on_deletion(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        beforeRows = self.fallbacksPage.count_total_rows()
        self.fallbacksPage.check_delete_button_functionality()
        afterRows = self.fallbacksPage.count_total_rows()
        assert str(beforeRows) != str(afterRows)

    def test_SNo_duplicate(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.check_SNo_duplicate() == True

    def test_download_CSV_Btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.get_downloaded_filePath(ConfigData.FALLBACKS_DOWNLOAD_CSV_FILE_PATH) == True

    def test_element_backgroundcolor_mousehover(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.get_element_background_Color() == 'rgba(0, 0, 0, 0)'

    def test_customer_chats_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.check_Customer_Chat_displayed() == True

    def test_create_intent_popup_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        assert self.fallbacksPage.check_Create_Intent_PopUp_displayed() == TestData.FALLBACKS_CREATE_INTENT_HEADER

    def test_create_intent_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        self.createIntentPage = CreateIntentPage(self.driver)
        intentName = TestDataFromExcel.readIntentVariable(self)
        newIntentName = intentName.split("_")[0] + "_" + str(int(intentName.split("_")[1]) + 1)

        TestDataFromExcel.write_in_excel('CreateIntent', 5, 1, newIntentName)
        New_IntentName = self.fallbacksPage.create_new_intent(intentName, 'yes')
        time.sleep(3)
        self.createIntentPage = self.homePage.click_intent_link()
        FallbackPage_IntentText = self.createIntentPage.get_first_intent_name()
        assert New_IntentName == FallbackPage_IntentText

    def test_select_all_CheckBox_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        self.fallbacksPage.click_select_all_checkbox_btn()
        assert self.fallbacksPage.check_select_all_checkbox_selected() == True

    def test_unselect_all_CheckBox_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.fallbacksPage = self.homePage.click_fallbacks_link()
        self.fallbacksPage.click_select_all_checkbox_btn()
        self.fallbacksPage.click_select_all_checkbox_btn()
        assert self.fallbacksPage.check_select_all_checkbox_selected() == False


