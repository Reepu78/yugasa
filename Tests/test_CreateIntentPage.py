import time

from Config.TestData import TestData
from Config.config import ConfigData
from TestData import ExcelLogic
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_CreateIntentPage(BaseTest):

    # def test_create_intent_page_displayed_correct(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
    #     self.createIntentPage = self.homePage.click_intent_link()
    #     assert self.createIntentPage.get_page_title_text() == TestData.CREATE_INTENT_PAGE_HEAD_TITLE

    def test_create_intent_page_displayed_correct(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.get_page_title_text() == TestData.CREATE_INTENT_PAGE_HEAD_TITLE


    def test_train_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.get_train_success_text() == TestData.TRAIN_SUCCESS_TEXT

    def test_add_intent_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.get_add_intent_popup_header_text() == TestData.ADD_INTENT_POPUP_HEAD_TEXT

    def test_add_value_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        Total_Add_Value_Expressions = self.createIntentPage.get_countof_AddValueExpressions()

        if Total_Add_Value_Expressions > 1:
            assert True
        else:
            assert False

    def test_text_response_accepts_allChar(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        intentName = TestDataFromExcel.readIntentVariable(self)
        newIntentName = intentName.split("_")[0] + "_" + str(int(intentName.split("_")[1]) + 1)
        TestDataFromExcel.write_in_excel('CreateIntent', 5, 1, newIntentName)
        assert self.createIntentPage.enter_text_in_Add_Intent_TextResponse(intentName, 'Tess&#@&^#*@287328739jhgdsjds') == True
        # assert self.createIntentPage.get_page_title_text() == TestData.CREATE_INTENT_PAGE_HEAD_TITLE

    def test_Add_Intent_Save_Btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        intentName = TestDataFromExcel.readIntentVariable(self)
        newIntentName = intentName.split("_")[0]+"_"+str(int(intentName.split("_")[1])+1)

        TestDataFromExcel.write_in_excel('CreateIntent', 5, 1, newIntentName)
        assert self.createIntentPage.click_add_intent_save_btn('test', intentName) == intentName.capitalize()

    def test_Add_Intent_DiscardBtn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.click_AddIntent_discard_btn() == True

    def test_edit_intent_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.click_edit_intent_btn() == TestData.EDIT_INTENT_HEADER_TEXT

    def test_active_inactive_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        self.createIntentPage.click_active_inactive_switch_btn()

    def test_delete_Intent_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.click_delete_btn() == True

    def test_check_download_btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        assert self.createIntentPage.click_download_csv_btn(ConfigData.INTENT_DOWNLOAD_CSV_FILE_PATH) == True

    def test_upload_file(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        time.sleep(20)
        assert self.createIntentPage.upload_file(ConfigData.INTENT_FILE_UPLOAD_PATH) == TestData.UPLOAD_INTENT_SUCCESS_MESSAGE

    def test_weak_strong_toggle_button_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.createIntentPage = self.homePage.click_intent_link()
        # var = TestDataFromExcel.readIntentVariable(self)
        intentName = TestDataFromExcel.readIntentVariable(self)
        newIntentName = intentName.split("_")[0] + "_" + str(int(intentName.split("_")[1]) + 1)

        TestDataFromExcel.write_in_excel('CreateIntent', 5, 1, newIntentName)
        assert self.createIntentPage.toggle_button_functionality(intentName, 'test') == True

