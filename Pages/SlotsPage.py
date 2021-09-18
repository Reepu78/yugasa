import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage
import pickle

class SlotsPage(BasePage):

    """Page Objects"""
    Page_Header = (By.CSS_SELECTOR, 'h1.main-title')
    Download_JSON_BTN = (By.CSS_SELECTOR, 'button.downloadjson')
    Download_JSON_Success_Msg = (By.CSS_SELECTOR, 'div.swal-text')
    ADD_SLOTS_BTN = (By.CSS_SELECTOR, 'button.add-slot')
    ADD_SLOTS_POPUP = (By.XPATH, "(//div[@class = 'modal-content  new-modal-content'])[2]")
    ADD_SLOTS_POPUP_Close_BTN = (By.XPATH, "(//div[@class = 'modal-content  new-modal-content'])[2]/div/button")
    ADD_SLOTS_POPUP_Close_BTN_MSG1 = (By.CSS_SELECTOR, 'div.swal-title')
    ADD_SLOTS_POPUP_Close_BTN_MSG2 = (By.CSS_SELECTOR, 'div.swal-text')
    ADD_SLOTS_POPUP_CLOSE_btn_CANCEL_BTN = (By.CSS_SELECTOR, 'button.swal-button--cancel')
    ADD_SLOTS_POPUP_CLOSE_btn_CANCEL_BTN_MSG = (By.CSS_SELECTOR, 'div.swal-text')
    ADD_SLOTS_POPUP_CLOSE_CANCEL_OK_BTN = (By.CSS_SELECTOR, 'button.swal-button--confirm')
    # Regex_ChckBox1 = (By.XPATH, "((//div[@class = 'modal-content  new-modal-content'])[2]/div[2]/div/div/div/div/div/input)[1]")
    Regex_ChckBox1 = (By.XPATH, "//*[@id='addslotregex']")
    Regex_ChckBox = (By.XPATH, "(//label[@class = 'new-box'])[2]")
    ADD_SLOTS_Title_field = (By.CSS_SELECTOR, 'input#add_tag')
    ADD_SLOTS_POPUP_SAVE_BTN = (By.CSS_SELECTOR, 'button.slot_save_button')
    ADD_SLOT_SUCCESS_MSG = (By.CSS_SELECTOR, 'div.swal-text')
    ADD_SLOTS_LABEL_field = (By.CSS_SELECTOR, 'input#addslotlabel')
    ADD_SLOTS_EXPRESSIONS_FIELD = (By.CSS_SELECTOR, 'input#add_expression')
    TOTAL_EXPRESSIONS_FIELD = (By.CSS_SELECTOR, 'div.add_input_fields_wrap')
    ADD_SLOTS_DISCARD_BTN = (By.XPATH, "(//button[@class = 'discard_Btn'])[2]")
    UPLOAD_JSON_SUCCESS_MSG = (By.CSS_SELECTOR, 'div.swal-text')
    TRAIN_BOT_BTN = (By.CSS_SELECTOR, 'button.trainslot')
    TRAIN_BOT_SUCCESS_MSG = (By.CSS_SELECTOR, 'div.swal-text')
    EDIT_SLOT_BTN = (By.XPATH, "(//i[@class = 'fa fa-edit'])[1]")
    EDIT_SLOTS_POPUP_HEAD = (By.XPATH, "(//h4[@id = 'exampleModalLabel'])[1]")
    EDIT_SLOTS_SAVE_BTN = (By.XPATH, "//button[@class = 'save_button']")
    Active_Inactive_Toggle_Btn = (By.XPATH, "(//span[@class = 'slider round-new'])[1]")
    SLOT_ACTIVE_INACTIVE_MSG = (By.CSS_SELECTOR, 'div.swal-title')
    SLOT_ACTIVE_INACTIVE_MSG_OK_Btn = (By.CSS_SELECTOR, 'button.swal-button--confirm')
    TOGGLE_BTN_VALUE = (By.XPATH, "(//label[@class = 'switch' and @title='Inactive'])[1]/input")
    DELETE_POPUP_CANCEL_BTN = (By.CSS_SELECTOR, 'button.swal-button--cancel')
    DELETE_POPUP_OK_BTN = (By.CSS_SELECTOR, 'button.swal-button--confirm')


    """Constructor of SlotsPage"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""
    def is_page_header_visible(self):
        return self.is_element_displayed(self.Page_Header)

    def click_download_json_btn(self, file_path):
        self.do_click(self.Download_JSON_BTN)
        time.sleep(3)
        if (self.is_visible(self.Download_JSON_Success_Msg)):
            return self.is_file_exist(file_path)
        else:
            return False

    def is_Add_Slots_popup_visible(self):
        self.do_click(self.ADD_SLOTS_BTN)
        return self.is_element_displayed(self.ADD_SLOTS_POPUP)

    def click_Add_Slots_PopUp_Close_Btn(self):
        self.do_click(self.ADD_SLOTS_BTN)
        time.sleep(1)
        self.driver.find_element_by_xpath("(//div[@class = 'modal-content  new-modal-content'])[2]/div/button").click()
        m1 = self.get_element_text(self.ADD_SLOTS_POPUP_Close_BTN_MSG1)
        m2 = self.get_element_text(self.ADD_SLOTS_POPUP_Close_BTN_MSG2)
        return [m1,m2]

    def click_Add_Slots_PopUp_CloseBtn_Cancel_Btn(self):
        self.do_click(self.ADD_SLOTS_BTN)
        time.sleep(1)
        self.driver.find_element_by_xpath("(//div[@class = 'modal-content  new-modal-content'])[2]/div/button").click()
        self.do_click(self.ADD_SLOTS_POPUP_CLOSE_btn_CANCEL_BTN)
        return self.get_element_text(self.ADD_SLOTS_POPUP_CLOSE_btn_CANCEL_BTN_MSG)

    def click_Add_Slots_PopUp_Close_Cancel_OK_Btn(self):
        self.do_click(self.ADD_SLOTS_BTN)
        time.sleep(1)
        self.driver.find_element_by_xpath("(//div[@class = 'modal-content  new-modal-content'])[2]/div/button").click()
        self.do_click(self.ADD_SLOTS_POPUP_CLOSE_btn_CANCEL_BTN)
        self.do_click(self.ADD_SLOTS_POPUP_CLOSE_CANCEL_OK_BTN)
        time.sleep(5)
        return self.is_element_displayed(self.ADD_SLOTS_POPUP)

    def check_Regex_Checkbox(self):
        self.do_click(self.ADD_SLOTS_BTN)
        time.sleep(5)
        # self.driver.find_element_by_xpath("((//div[@class = 'modal-content  new-modal-content'])[2]/div[2]/div/div/div/div/div/input)[1]").click()
        return self.is_element_displayed(self.Regex_ChckBox1)
        # self.do_click(self.Regex_ChckBox)
        # if self.get_element_attribute(self.Regex_ChckBox, 'value') ==1:
        #     return True
        # else:
        #     return False

    def input_in_title_field(self, title_name):
        self.do_click(self.ADD_SLOTS_BTN)
        self.do_send_keys(self.ADD_SLOTS_Title_field, title_name)
        self.do_click(self.ADD_SLOTS_POPUP_SAVE_BTN)
        return self.get_element_text(self.ADD_SLOT_SUCCESS_MSG)

    def input_in_label_fielf(self):
        self.do_click(self.ADD_SLOTS_BTN)
        self.do_send_keys(self.ADD_SLOTS_LABEL_field, 'Label1')
        self.do_click(self.ADD_SLOTS_POPUP_SAVE_BTN)
        return self.get_element_text(self.ADD_SLOT_SUCCESS_MSG)

    def input_in_expression_field(self):
        self.do_click(self.ADD_SLOTS_BTN)
        self.do_send_keys(self.ADD_SLOTS_EXPRESSIONS_FIELD, 'expression1')
        self.driver.find_element_by_css_selector('input#add_expression').send_keys(Keys.ENTER)
        NumofExpressions = self.get_all_elements(self.TOTAL_EXPRESSIONS_FIELD)
        if len(NumofExpressions)>1:
            self.do_click(self.ADD_SLOTS_POPUP_SAVE_BTN)
            return self.get_element_text(self.ADD_SLOT_SUCCESS_MSG)
        else:
            return False

    def click_ADD_SLOTS_SAVE_Btn_functionality(self,title_name):
        self.do_click(self.ADD_SLOTS_BTN)
        self.do_send_keys(self.ADD_SLOTS_Title_field, title_name)
        self.do_send_keys(self.ADD_SLOTS_LABEL_field, 'Label1')
        self.do_send_keys(self.ADD_SLOTS_EXPRESSIONS_FIELD, 'expression1')
        self.do_click(self.ADD_SLOTS_POPUP_SAVE_BTN)
        return self.get_element_text(self.ADD_SLOT_SUCCESS_MSG)

    def click_ADD_SLOT_Discard_Btn(self):
        self.do_click(self.ADD_SLOTS_BTN)
        self.do_click(self.ADD_SLOTS_DISCARD_BTN)
        m1 = self.get_element_text(self.ADD_SLOTS_POPUP_Close_BTN_MSG1)
        m2 = self.get_element_text(self.ADD_SLOTS_POPUP_Close_BTN_MSG2)
        return [m1, m2]

    def check_Upload_JSON_file(self, filePath):
        self.driver.find_element_by_css_selector('input#loadSlotJson').send_keys(filePath)
        return self.get_element_text(self.UPLOAD_JSON_SUCCESS_MSG)

    def click_Train_Bot_Btn(self):
        self.do_click(self.TRAIN_BOT_BTN)
        return self.get_element_text(self.TRAIN_BOT_SUCCESS_MSG)

    def click_edit_slot_btn(self):
        self.do_click(self.EDIT_SLOT_BTN)
        return self.is_clickable(self.EDIT_SLOTS_SAVE_BTN)
        # return self.is_element_displayed(self.EDIT_SLOTS_POPUP_HEAD)

    def click_toggle_btn_Active(self):
        self.do_click(self.Active_Inactive_Toggle_Btn)
        return self.get_element_text(self.SLOT_ACTIVE_INACTIVE_MSG)
        # self.do_click(self.SLOT_ACTIVE_INACTIVE_MSG_OK_Btn)

    def click_toggle_btn_InActive(self):
        self.do_click(self.Active_Inactive_Toggle_Btn)
        self.do_click(self.SLOT_ACTIVE_INACTIVE_MSG_OK_Btn)
        self.do_click(self.Active_Inactive_Toggle_Btn)
        return self.get_element_text(self.SLOT_ACTIVE_INACTIVE_MSG)

    def click_delete_btn(self):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.get_element(self.EDIT_SLOT_BTN), 60,
        0).click().perform()
        return self.is_element_displayed(self.DELETE_POPUP_OK_BTN) and self.is_element_displayed(self.DELETE_POPUP_CANCEL_BTN)





























