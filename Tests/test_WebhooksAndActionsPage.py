import time
from Pages.LoginPage import LoginPage
from TestData.ExcelLogic import TestDataFromExcel
from Tests.test_base import BaseTest
import random
from Pages.WebhooksAndActions import WebhooksAndActions
from benchexec.tools import false


class Test_WebhooksAndActionsPage(BaseTest):

    def test_page_header_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True

    def test_verify_webhooks(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True

    def test_verify_actions_btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addAction =self.webHooks.click_On_Add_Action_Btn()
        assert self.addAction.check_Page_Add_Action_display() == True

    def test_verify_discard_confirmation_message(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True
        num = random.randint(0,999)
        string_value = str(num)
        text = "test {}"
        self.addHook.enter_name(text.format(string_value))
        self.addHook.enter_url("www.demotest.com")
        self.addHook.enter_parameters("Hooks_parameters")
        self.addHook.enter_API("Key")
        self.addHook.enter_API_Secret("APi")
        self.addHook.select_Method()
        self.addHook.click_On_Discard_Btn()
        assert false == True, 'Confirmation Message not displayed'

    def test_verify_click_Ok_discard_confirmation_message(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True
        num = random.randint(0,999)
        string_value = str(num)
        text = "test {}"
        self.addHook.enter_name(text.format(string_value))
        self.addHook.enter_url("www.demotest.com")
        self.addHook.enter_parameters("Hooks_parameters")
        self.addHook.enter_API("Key")
        self.addHook.enter_API_Secret("APi")
        self.addHook.select_Method()
        self.addHook.click_On_Discard_Btn()
        assert false==True, 'ok button not displayed'

    def test_verify_click_cancel_discard_confirmation_message(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True
        num = random.randint(0,999)
        string_value = str(num)
        text = "test {}"
        self.addHook.enter_name(text.format(string_value))
        self.addHook.enter_url("www.demotest.com")
        self.addHook.enter_parameters("Hooks_parameters")
        self.addHook.enter_API("Key")
        self.addHook.enter_API_Secret("APi")
        self.addHook.select_Method()
        self.addHook.click_On_Discard_Btn()
        assert false == True, 'Cancel button not displayed'


    def test_verify_create_an_action(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        num = random.randint(0, 999)
        string_value = str(num)
        text = "ActionDemo {}"
        self.add_Action.enter_Action_Name(text.format(string_value))
        self.add_Action.enter_Action_Url("www.actionTest.com")
        self.add_Action.enter_Action_Header("ActionHeader")
        self.add_Action.enter_Action_Data_Body("Action Data")
        self.add_Action.select_Action_Method()
        self.add_Action.select_Your_Action_Slots()
        self.add_Action.enter_Action_Response("Response1")
        self.add_Action.enter_Second_Action_Response("Response2")
        self.add_Action.click_On_Action_save_Btn()
        time.sleep(5)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True

    def test_verify_action_drop_down_method(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        num = random.randint(0, 999)
        string_value = str(num)
        text = "ActionDemo {}"
        self.add_Action.enter_Action_Name(text.format(string_value))
        self.add_Action.enter_Action_Url("www.actionTest.com")
        self.add_Action.enter_Action_Header("ActionHeader")
        self.add_Action.enter_Action_Data_Body("Action Data")
        self.add_Action.select_Action_Method()
        self.add_Action.select_Your_Action_Slots()
        self.add_Action.enter_Action_Response("Response1")
        self.add_Action.enter_Second_Action_Response("Response2")
        self.add_Action.click_On_Action_save_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True

    def test_verify_multiple_response_add_in_an_action(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        num = random.randint(0, 999)
        string_value = str(num)
        text = "ActionDemo {}"
        self.add_Action.enter_Action_Name(text.format(string_value))
        self.add_Action.enter_Action_Url("www.actionTest.com")
        self.add_Action.enter_Action_Header("ActionHeader")
        self.add_Action.enter_Action_Data_Body("Action Data")
        self.add_Action.select_Action_Method()
        self.add_Action.select_Your_Action_Slots()
        self.add_Action.enter_Action_Response("Response1")
        self.add_Action.enter_Second_Action_Response("Response2")
        self.add_Action.click_On_Add_Response_Btn()
        self.add_Action.enter_Third_Action_Response("Response3")
        self.add_Action.enter_Fourth_Action_Response("Response4")
        self.add_Action.click_On_Action_save_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
        time.sleep(5)

    def test_verify_multiple_response_remove_in_an_action(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        num = random.randint(0, 999)
        string_value = str(num)
        text = "ActionDemo {}"
        self.add_Action.enter_Action_Name(text.format(string_value))
        self.add_Action.enter_Action_Url("www.actionTest.com")
        self.add_Action.enter_Action_Header("ActionHeader")
        self.add_Action.enter_Action_Data_Body("Action Data")
        self.add_Action.select_Action_Method()
        self.add_Action.select_Your_Action_Slots()
        self.add_Action.enter_Action_Response("Response1")
        self.add_Action.enter_Second_Action_Response("Response2")
        self.add_Action.click_On_Add_Response_Btn()
        self.add_Action.enter_Third_Action_Response("Response3")
        self.add_Action.enter_Fourth_Action_Response("Response4")
        self.add_Action.click_On_Action_save_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
        self.add_Action.click_On_Sub_Response_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Update_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
        time.sleep(3)

    def test_verify_deleted_response_not_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        num = random.randint(0, 999)
        string_value = str(num)
        text = "ActionDemo {}"
        self.add_Action.enter_Action_Name(text.format(string_value))
        self.add_Action.enter_Action_Url("www.actionTest.com")
        self.add_Action.enter_Action_Header("ActionHeader")
        self.add_Action.enter_Action_Data_Body("Action Data")
        self.add_Action.select_Action_Method()
        self.add_Action.select_Your_Action_Slots()
        self.add_Action.enter_Action_Response("Response1")
        self.add_Action.enter_Second_Action_Response("Response2")
        self.add_Action.click_On_Add_Response_Btn()
        self.add_Action.enter_Third_Action_Response("Response3")
        self.add_Action.enter_Fourth_Action_Response("Response4")
        self.add_Action.click_On_Action_save_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
        self.add_Action.click_On_Sub_Response_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Update_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
        time.sleep(3)

    def test_verify_ok_confirmation_button(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        self.add_Action.click_On_Action_Discard_Btn()
        assert false == True, 'Cancel button not displayed'

    def test_verify_cancel_button_action(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        self.add_Action.click_On_Action_Discard_Btn()
        assert false == True, 'Cancel button not displayed'

    def test_verify_edit_Icon_is_Working(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
        time.sleep(3)
        self.add_Action.enter_Action_New_Url("www.UpdateActionTest.com")
        self.add_Action.click_On_Action_Update_Btn()
        time.sleep(3)
        self.add_Action.click_On_Action_Edit_Icon()
        assert self.add_Action.verify_Action_Data_Add_in_Action_Page() == True
































