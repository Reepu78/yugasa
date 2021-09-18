import time

from Pages.LoginPage import LoginPage
from TestData.ExcelLogic import TestDataFromExcel
from Tests.test_base import BaseTest
import random

from Pages.WebhooksAndActions import WebhooksAndActions


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
    #     codecomplete


    def test_verify_actions_btn(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addAction =self.webHooks.click_On_Add_Action_Btn()
        assert self.addAction.check_Page_Add_Action_display() == True

    #     codecomplete

    def test_verify_add_webhook_is_working_properly(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True
        num=random.randint(0,999)
        string_value = str(num)
        text = "test {}"
        self.addHook.enter_name(text.format(string_value))
        self.addHook.enter_url("www.demotest.com")
        self.addHook.enter_parameters("Hooks_parameters")
        self.addHook.enter_API("key")
        self.addHook.enter_API_Secret("demoKey")
        self.addHook.select_Method()
        self.addHook.click_On_Save_Btn()
        time.sleep(3)
        self.addHook.click_On_Edit_Icon()
        assert self.addHook.check_page_Edit_WebHook() == True
        # code complete
        # not click edit icon of webhook

    def test_verify_mandotry_filed(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True
        self.addHook.enter_name(" ")
        self.addHook.enter_url("www.demotest.com")
        self.addHook.enter_parameters("Hooks_parameters")
        self.addHook.enter_API("Key")
        self.addHook.enter_API_Secret("APi")
        self.addHook.select_Method()
        time.sleep(3)
        self.addHook.click_On_Save_Btn()
        time.sleep(3)
       # pending verify popUp error Message


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
        # code complete
    #     wrong step in excel sheet

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

    # code complete
    #     wrong step in excel sheet

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

    # code complete
    #     wrong step in excel sheet

    def test_verify_edit_button_is_working(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.editIcon = WebhooksAndActions(self.driver)
        time.sleep(3)
        self.editIcon.click_On_Edit_Icon() # edit icon  is not clicking
        assert self.editIcon.check_page_Edit_WebHook_display() == True
        self.editIcon.enter_New_Url("www.newdemoTest.com")
        time.sleep(3)
        self.editIcon.click_On_Update_Btn()
        time.sleep(3)
        self.editIcon.click_On_Edit_Icon()
        assert self.editIcon.check_Page_AddHook_display() == True
        # Code complete


    def test_verify_delete_button_is_working(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.deleteIcon = WebhooksAndActions(self.driver)
        time.sleep(3)
        self.deleteIcon.click_On_Delete_Icon() # delete icon is not clicking
        assert self.deleteIcon.check_Page_Delete_Display() == True
        time.sleep(3)
        self.deleteIcon.click_On_Delete_Ok_Btn()
        assert self.deleteIcon.check_Page_Header_display() == True
         # code complete

    def test_verify_empty_webhook_not_get_created(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addWebHook = WebhooksAndActions(self.driver)
        self.addWebHook.click_On_WebHook_Btn()
        assert self.addWebHook.check_Page_AddHook_display()==True
        self.addWebHook.click_On_Save_Btn()

      #  popUp message not display


    def test_verify_drop_down_method_add(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.addHook = self.webHooks.click_On_WebHook_Btn()
        assert self.addHook.check_Page_AddHook_display() == True
        num = random.randint(0, 999)
        string_value = str(num)
        text = "test {}"
        self.addHook.enter_name(text.format(string_value))
        self.addHook.enter_url("www.demotest.com")
        self.addHook.enter_parameters("Hooks_parameters")
        self.addHook.enter_API("key")
        self.addHook.enter_API_Secret("demoKey")
        self.addHook.select_Method()
        self.addHook.click_On_Save_Btn()
        time.sleep(3)
        self.addHook.click_On_Edit_Icon() # edit icon not clicking
        assert self.addHook.check_page_Edit_WebHook() == True
        # code complete
        # ask for verification

    def test_verify_empty_action_not_created(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action= WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        self.add_Action.click_On_Action_save_Btn()

        #  popUp message not display

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
        # code complate

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
        # code complete

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
        # code complete

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
        # code complete


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
        # code complete

    def test_verify_ok_confirmation_button(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        self.add_Action.click_On_Action_Discard_Btn()
        assert self.add_Action.check_Page_Header_display() == True
        # code complete
        # wrong step in excel sheet

    def test_verify_cancel_button_action(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        self.add_Action.click_On_Add_Action_Btn()
        assert self.add_Action.check_Page_Add_Action_display() == True
        self.add_Action.click_On_Action_Discard_Btn()
        assert self.add_Action.check_Page_Header_display() == True
        # code complete
        # wrong step in excel sheet

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
        # code complete

    def test_verify_delete_Icon_is_Working(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.webHooks = self.homePage.click_leftMenu_Webhooks_and_Actions()
        assert self.webHooks.check_Page_Header_display() == True
        self.add_Action = WebhooksAndActions(self.driver)
        time.sleep(3)
        self.add_Action.click_On_Delete_Icon_Action()
        assert self.add_Action.check_Page_Delete_Display() == True
        self.add_Action.click_On_Delete_Ok_Btn()
        assert self.add_Action.check_Page_Header_display() == True
        # code complete
        # not clicking on delete icon of action
































