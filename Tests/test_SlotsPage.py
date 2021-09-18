from Config.TestData import TestData
from Config.config import ConfigData
from Pages.LoginPage import LoginPage
from TestData.ExcelLogic import TestDataFromExcel
from Tests.test_base import BaseTest


class Test_SlotsPage(BaseTest):

    def test_pageHeader_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.is_page_header_visible() == True

    def test_download_JSON_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_download_json_btn(ConfigData.SLOTS_DOWNLOAD_JSON_FILE_PATH) == True

    def test_check_Add_Slots_PopUp_Display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.is_Add_Slots_popup_visible() == True

    def test_Add_Slots_PopUp_Close_Btn_Msg(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_Add_Slots_PopUp_Close_Btn() == [TestData.ADD_SLOTS_CANCEL_BTN_MSG1,TestData.ADD_SLOTS_CANCEL_BTN_MSG2]

    def test_Add_Slots_PopUp_CloseBtn_Cancel_Btn_Msg(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_Add_Slots_PopUp_CloseBtn_Cancel_Btn() == TestData.ADD_SLOTS_CANCELBTN_CLOSE_BTN_MSG

    def test_Add_Slots_PopUp_Close_Cancel_OK_Btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_Add_Slots_PopUp_Close_Cancel_OK_Btn() == False

    # def test_Regex_CheckBox_check(self):
    #     self.loginPage = LoginPage(self.driver)
    #     self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
    #     self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
    #     assert self.slotsPage.check_Regex_Checkbox() == True

    def test_add_title_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        titleName = TestDataFromExcel.read_addSlot_title_variable(self)
        newTitleName = titleName.split("_")[0] + "_" + str(int(titleName.split("_")[1]) + 1)
        TestDataFromExcel.write_in_excel('SLOTSPAGE', 2, 1, newTitleName)
        assert self.slotsPage.input_in_title_field(titleName) == TestData.ADD_SLOTS_SUCCEESS_MSG

    def test_add_label_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.input_in_label_fielf() == TestData.ADD_SLOTS_SUCCEESS_MSG

    def test_add_expressions_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.input_in_expression_field() == TestData.ADD_SLOTS_SUCCEESS_MSG

    def test_Save_Btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        titleName = TestDataFromExcel.read_addSlot_title_variable(self)
        newTitleName = titleName.split("_")[0] + "_" + str(int(titleName.split("_")[1]) + 1)
        TestDataFromExcel.write_in_excel('SLOTSPAGE', 2, 1, newTitleName)
        assert self.slotsPage.click_ADD_SLOTS_SAVE_Btn_functionality(titleName) == TestData.ADD_SLOTS_SUCCEESS_MSG

    def test_Add_Slot_Discard_Btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_ADD_SLOT_Discard_Btn() == [TestData.ADD_SLOTS_CANCEL_BTN_MSG1,TestData.ADD_SLOTS_CANCEL_BTN_MSG2]

    def test_Upload_JSON_BTN_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.check_Upload_JSON_file(ConfigData.SLOTS_FILE_UPLOAD_PATH) == TestData.UPLOAD_JSON_SUCCESS_MESSAGE

    def test_Train_Bot_Btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_Train_Bot_Btn() == TestData.TRAIN_BOT_SUCCESS_MESSAGE

    def test_Download_JSON_BTN_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_download_json_btn(ConfigData.SLOTS_DOWNLOAD_JSON_FILE_PATH) == True

    def test_edit_slot_btn_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_edit_slot_btn() == True
    
    def test_toggle_btn_InActive_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_toggle_btn_InActive() == TestData.TOGGLE_ACTIVE_MSG
    
    def test_toggle_btn_Active_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_toggle_btn_Active() == TestData.TOGGLE_INACTIVE_MSG

    def test_delete_btn_popUp(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.slotsPage = self.homePage.click_leftMenu_SlotsLink()
        assert self.slotsPage.click_delete_btn() == True









