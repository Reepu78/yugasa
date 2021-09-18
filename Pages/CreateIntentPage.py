import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage


class CreateIntentPage(BasePage):
    """By Locators"""

    Page_Head_Title = (By.CSS_SELECTOR, 'h1.main-title')
    Train_Btn = (By.CSS_SELECTOR, 'button.trainBtn')
    Train_Success_Text = (By.CSS_SELECTOR, 'div.swal-text')
    Add_Intent_Btn = (By.CSS_SELECTOR, 'button.add-intent')
    Add_Intent_PopUp_Head_Text = (By.XPATH, "(//h4[@id = 'exampleModalLabel'])[2]")
    Add_Value_Expression_Default = (By.CSS_SELECTOR, 'input#add_expression')
    Total_Add_Value_Expression = (By.CSS_SELECTOR, 'div.add_input_fields_wrap')
    Add_Intent_TextResponse = (By.CSS_SELECTOR, 'textarea#add_textresp')
    Add_Intent_Save_Btn = (By.XPATH, "//*[@id='add_intent']/div/div/div[2]/div[2]/div/div/button[2]")
    Add_Intent_Intent_Name = (By.XPATH, "(//input[contains(@id , 'tag')])[2]")
    Add_intent_Weak_Strong_Toggle_Button = (By.XPATH, "(//span[@class = 'slider_intent round_intent'])[2]")
    Edit_Intent_Weak_Strong_Toggle_Button = (By.XPATH, "(//span[@class = 'slider_intent round_intent'])[1]")
    Edit_Intent_Text_Response = (By.CSS_SELECTOR, 'textarea#textresp')
    First_Position_Intent_Title = (By.XPATH, "//div[@id = '0']")
    First_Position_Intent_Edit_Btn = (By.XPATH, "(//i[@class = 'fa fa-edit'])[1]")
    Add_Intent_Discard_Btn = (By.XPATH, "(// button[@class ='discard_Btn'])[2]")
    Add_Intent_Discard_PopUp = (By.CSS_SELECTOR, 'div.swal-modal')
    Edit_Intent_Header = (By.XPATH, "(//h4[@id = 'exampleModalLabel'])[1]")
    Active_Inactive_Switch_Btn = (By.XPATH, "(//span[@class = 'slider round-new'])[1]")
    Delete_Btn = (By.XPATH, "(//i[@class = 'fa fa-trash-o'])[1]")
    Delete_PopUp_Head = (By.CSS_SELECTOR, 'div.swal-text')
    Delete_PopUp_OK_Btn = (By.CSS_SELECTOR, 'button.swal-button--confirm')
    Delete_PopUp_Cancel_Btn = (By.CSS_SELECTOR, 'button.swal-button--cancel')
    Download_CSV_Btn = (By.CSS_SELECTOR, 'button.intent_excel')
    Upload_Btn = (By.CSS_SELECTOR, 'input#loadIntent')
    Upload_Intent_Success_Msg = (By.CSS_SELECTOR, 'div.swal-text')

    """Page Actions"""

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title_text(self):
        return self.get_element_text(self.Page_Head_Title)

    def get_train_success_text(self):
        time.sleep(10)
        self.do_click(self.Train_Btn)
        time.sleep(30)
        return self.get_element_text(self.Train_Success_Text)

    def get_add_intent_popup_header_text(self):
        self.do_click(self.Add_Intent_Btn)
        return self.get_element_text(self.Add_Intent_PopUp_Head_Text)

    def input_text_add_value_expression(self):
        self.do_click(self.Add_Intent_Btn)
        self.do_send_keys(self.Add_Value_Expression_Default, 'Hi')
        self.do_send_keys(self.Add_Value_Expression_Default, Keys.ENTER)

    def get_countof_AddValueExpressions(self):
        self.input_text_add_value_expression()
        return self.get_countof_elements_in_list(self.Total_Add_Value_Expression)

    def enter_text_in_Add_Intent_TextResponse(self, IntentName_Text, TextResponse_text):
        self.do_click(self.Add_Intent_Btn)
        self.do_send_keys(self.Add_Intent_TextResponse, TextResponse_text)
        self.do_send_keys(self.Add_Intent_Intent_Name, IntentName_Text)
        self.do_send_keys(self.Add_Value_Expression_Default, 'Hi')
        self.do_click(self.Add_Intent_Save_Btn)
        time.sleep(3)
        if self.get_element_text(self.First_Position_Intent_Title) == IntentName_Text:
            self.do_click(self.First_Position_Intent_Edit_Btn)
        if self.get_element_text(self.Edit_Intent_Text_Response) == TextResponse_text:
            return True
        else:
            return False

    def click_add_intent_save_btn(self, TextResponse_text, IntentName):
        self.do_click(self.Add_Intent_Btn)
        self.do_send_keys(self.Add_Intent_TextResponse, TextResponse_text)
        self.do_send_keys(self.Add_Intent_Intent_Name, IntentName)
        self.do_send_keys(self.Add_Value_Expression_Default, 'Hi')
        self.do_click(self.Add_Intent_Save_Btn)
        time.sleep(5)

        return self.get_element_text(self.First_Position_Intent_Title)

    def get_first_intent_name(self):
        return self.get_element_text(self.First_Position_Intent_Title)

    def click_AddIntent_discard_btn(self):
        self.do_click(self.Add_Intent_Btn)
        self.do_click(self.Add_Intent_Discard_Btn)
        return self.is_visible(self.Add_Intent_Discard_PopUp)

    def click_edit_intent_btn(self):
        self.do_click(self.First_Position_Intent_Edit_Btn)
        if self.is_visible(self.Edit_Intent_Header):
            return self.get_element_text(self.Edit_Intent_Header)

    def click_active_inactive_switch_btn(self):
        self.is_clickable(self.Active_Inactive_Switch_Btn)
        self.do_click(self.Active_Inactive_Switch_Btn)

    def toggle_button_functionality(self, IntentName, TextResponse_text):
        self.do_click(self.Add_Intent_Btn)
        self.do_send_keys(self.Add_Intent_Intent_Name, IntentName)
        self.do_send_keys(self.Add_Intent_TextResponse, TextResponse_text)
        self.do_send_keys(self.Add_Value_Expression_Default, 'Hi')
        self.do_click(self.Add_intent_Weak_Strong_Toggle_Button)
        self.do_click(self.Add_Intent_Save_Btn)
        time.sleep(3)
        if self.get_element_text(self.First_Position_Intent_Title) == IntentName:
            self.do_click(self.First_Position_Intent_Edit_Btn)

        return self.is_element_selected(self.Edit_Intent_Weak_Strong_Toggle_Button)

    def click_delete_btn(self):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.get_element(self.First_Position_Intent_Edit_Btn), 60,
        0).click().perform()
        return self.is_element_displayed(self.Delete_PopUp_OK_Btn) and self.is_element_displayed(self.Delete_PopUp_Cancel_Btn)


    def click_download_csv_btn(self, file_path):
        self.do_click(self.Download_CSV_Btn)
        time.sleep(3)
        return self.is_file_exist(file_path)

    def click_Upload(self):
        self.do_click(self.Upload_Btn)

    def upload_file(self, filePath):
        # self.do_send_keys(self.Upload_Btn, filePath)
        # self.Upload_Btn.send_keys(filePath)
        self.driver.find_element_by_css_selector('input#loadIntent').send_keys(filePath)
        time.sleep(10)
        return self.get_element_text(self.Upload_Intent_Success_Msg)
