import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from selenium.webdriver.support import wait


class WebhooksAndActions(BasePage):

    """Page Actions"""
    Page_Header = (By.XPATH, "//h3[text() = 'Webhooks and Actions']")
    Delete_Ok_Btn = (By.XPATH, "//*[@class='swal-button swal-button--confirm swal-button--danger']")

    Page_Add_Action = (By.XPATH, "(//*[@id='exampleModalLabel'])[2]")
    Add_Action_Btn = (By.XPATH, "//*[@class='btn btn-secondary add-actions add_actions']")
    Page_Add_WebHook = (By.XPATH, "(//*[@id='exampleModalLabel'])[1]")
    Add_Webhook_Btn = (By.XPATH, "//*[@class='btn btn-secondary add-intent add_webhook']")
    Webhooks_Name = (By.XPATH, "//*[@id='wName']")
    Webhooks_Url = (By.XPATH, "//*[@id='wUrl']")
    Webhooks_Parameters = (By.XPATH, "//*[@id='wParameters']")
    Webhooks_API = (By.XPATH, "//*[@id='wApiKey']")
    WebhooksAPI_Secret = (By.XPATH, "//*[@id='wApiScrtKey']")
    Webhooks_Method = (By.XPATH, "//*[@id='wRqwstMthd']")
    Webhooks_Post_Method = (By.XPATH, "(//*[@id='wRqwstMthd']/*)[2]")
    Webhooks_Save_Btn = (By.XPATH, "(//*[@class='save_button'])[1]")
    Webhooks_Discard_btn =(By.XPATH,"(//*[@class='discard_Btn'])[1]")
    # Webhooks_Edit_Icon = (By.XPATH, "(//div[@class='editWebhook'])[1]/*")
    Webhooks_Edit_Icon = (By.XPATH, "//*[@xpath='1']")
    Page_Edit_WebHook = (By.XPATH, "(//*[@id='exampleModalLabel'])[3]")
    Webhooks_Update_Url =(By.XPATH, "//*[@id='webhookUrl']")
    Webhooks_Update_Btn = (By.XPATH,"(//*[@class='save_button'])[2]")
    Webhooks_Delete_Icon = (By.XPATH, "(//*[@class='fa fa-trash-o'])[1]")
    Page_delete = (By.XPATH,"//*[text()='Are you sure?']")


    # location of an action element
    Action_Name = (By.XPATH,"//*[@id='actnName']")
    Action_Url = (By.XPATH,"//*[@id='actnUrl']")
    Action_Update_Url =(By.XPATH,"//*[@id='actionUrl']")
    Action_Header = (By.XPATH,"//*[@id='actnHeaders']")
    Action_Body_Data = (By.XPATH,"//*[@id='actnData']")
    Action_Method = (By.XPATH,"//*[@id='actnRqwstMthd']")
    Action_Post_Method = (By.XPATH,"(//*[@id='actnRqwstMthd']/*)[2]")
    Action_Slots = (By.XPATH,"//*[@class='chosen-choices']")
    Action_Slots_Product = (By.XPATH,"(//*[@class='chosen-drop']/*/*)[1]")
    Action_Response_Box= (By.XPATH,"(//*[@class='form-control inputkey'])[1]")
    Action_Second_Response_Box = (By.XPATH,"(//*[@class='form-control inputvalue'])[1]")
    Action_Third_Response_Box = (By.XPATH,"(//*[@class='form-control inputkey'])[2]")
    Action_Fourth_Response_Box = (By.XPATH,"(//*[@class='form-control inputvalue'])[2]")
    Action_Add_New_Response_Box = (By.XPATH,"//*[@class='add_form_field btn br5 addresp']")
    Action_Sub_Response_Box = (By.XPATH,"//*[@class='editdelteformfiled btn br5']")
    Action_Save_Btn = (By.XPATH,"//*[@class='save_button  actionsave']")
    Action_Discard_Btn = (By.XPATH,"(//*[@class='discard_Btn'])[2]")
    Action_Edit_Icon = (By.XPATH,"(//*[@class='editAction']/*)[1]")
    Page_Edit_Action = (By.XPATH,"(//*[@id='exampleModalLabel'])[4]")
    Action_Update_Btn = (By.XPATH,"(//*[@class='save_button'])[3]")
    Action_Delete_Icon = (By.XPATH,"(//*[@class='fa fa-trash-o'])[2]")
    Page_Delete_Action = (By.XPATH,"//*[text()='Are you sure?']")









    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""
    def check_Page_Header_display(self):
       return self.is_element_displayed(self.Page_Header)

# def of AddWebHooks

    def click_On_WebHook_Btn(self):
        self.do_click(self.Add_Webhook_Btn)
        return WebhooksAndActions(self.driver)

    def check_Page_AddHook_display(self):
        return self.is_element_displayed(self.Page_Add_WebHook)


    def enter_name(self,WebHookName):
        self.do_send_keys(self.Webhooks_Name,WebHookName)

    def enter_url(self,WebHookUrl):
        self.do_send_keys(self.Webhooks_Url,WebHookUrl)

    def enter_parameters(self,WebHookParameters):
        self.do_send_keys(self.Webhooks_Parameters,WebHookParameters)

    def enter_API(self,WebHookAPI):
        self.do_send_keys(self.Webhooks_API,WebHookAPI)

    def enter_API_Secret(self,WebHookAPISecret):
        self.do_send_keys(self.WebhooksAPI_Secret,WebHookAPISecret)

    def select_Method(self):
        self.do_click(self.Webhooks_Method)
        self.do_click(self.Webhooks_Post_Method)

    def click_On_Save_Btn(self):
        self.do_click(self.Webhooks_Save_Btn)

    def click_On_Discard_Btn(self):
        self.do_click(self.Webhooks_Discard_btn)

    def click_On_Edit_Icon(self):
        self.do_click(self.Webhooks_Edit_Icon)

    def check_page_Edit_WebHook_display(self):
        return self.is_element_displayed(self.Page_Edit_WebHook)

    def enter_New_Url(self,NewUrl):
        self.clear_element(self.Webhooks_Update_Url)
        self.do_send_keys(self.Webhooks_Update_Url, NewUrl)

    def click_On_Update_Btn(self):
        self.do_click(self.Webhooks_Update_Btn)

    def click_On_Delete_Icon(self):
        self.do_click(self.Webhooks_Delete_Icon)

    def check_Page_Delete_Display(self):
        return self.is_element_displayed(self.Page_delete)

    def click_On_Delete_Ok_Btn(self):
        self.do_click(self.Delete_Ok_Btn)


#    def. of Add Action
    def click_On_Add_Action_Btn(self):
        self.do_click(self.Add_Action_Btn)
        return WebhooksAndActions(self.driver)

    def check_Page_Add_Action_display(self):
        return self.is_element_displayed(self.Page_Add_Action)

    def enter_Action_Name(self, actionName):
        self.do_send_keys(self.Action_Name,actionName)

    def enter_Action_Url(self, actionUrl):
        self.do_send_keys(self.Action_Url,actionUrl)

    def enter_Action_New_Url(self, newActionUrl):
        self.clear_element(self.Action_Update_Url)
        self.do_send_keys(self.Action_Update_Url, newActionUrl)

    def enter_Action_Header(self,actionHeader):
        self.do_send_keys(self.Action_Header,actionHeader)

    def enter_Action_Data_Body(self,actionData):
        self.do_send_keys(self.Action_Body_Data,actionData)

    def select_Action_Method(self):
        self.do_click(self.Action_Method)
        self.do_click(self.Action_Post_Method)

    def select_Your_Action_Slots(self):
        self.do_click(self.Action_Slots)
        self.do_click(self.Action_Slots_Product)

    def enter_Action_Response(self,response1):
        self.do_send_keys(self.Action_Response_Box,response1)

    def enter_Second_Action_Response(self,response2):
        self.do_send_keys(self.Action_Second_Response_Box,response2)

    def click_On_Action_save_Btn(self):
        self.do_click(self.Action_Save_Btn)

    def click_On_Action_Discard_Btn(self):
        self.do_click(self.Action_Discard_Btn)



    def click_On_Action_Edit_Icon(self):
        self.do_click(self.Action_Edit_Icon)
        # return WebhooksAndActions(self.driver)

    def verify_Action_Data_Add_in_Action_Page(self):
        return self.is_element_displayed(self.Page_Edit_Action)

    def click_On_Add_Response_Btn(self):
        self.do_click(self.Action_Add_New_Response_Box)

    def enter_Third_Action_Response(self,response3):
        self.do_send_keys(self.Action_Third_Response_Box,response3)

    def enter_Fourth_Action_Response(self, response4):
            self.do_send_keys(self.Action_Fourth_Response_Box, response4)

    def click_On_Sub_Response_Btn(self):
        self.do_click(self.Action_Sub_Response_Box)

    def click_On_Action_Update_Btn(self):
        self.do_click(self.Action_Update_Btn)

    def click_On_Delete_Icon_Action(self):
        self.do_click(self.Action_Delete_Icon)
        # return WebhooksAndActions(self.driver)


























        # self.Webhooks_Name.send_keys("testdemo1")
        # time.sleep(3)
        # self.driver.find_element_by_xpath(self.Webhooks_Name).send_keys(name)
        # time.sleep(3)
        # # self.Webhooks_Url.send_keys("www.testdemo.com")
        # # self.Webhooks_Parameters.send_keys("demotest")
        # # self.Webhooks_API.send_keys("API")
        # # self.Webhooks_Method.send_keys("POST")
        # # self.do_clcick(self.Webhooks_Save)
        #
        #






