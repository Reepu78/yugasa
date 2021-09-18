import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class FallbacksPage(BasePage):
    """By Locator"""

    Actions_Ignore_Btn = (By.XPATH, "(//*[@id = 'ignore'])[1]")
    Actions_Ignore_Btn_PopUp_Title = (By.CSS_SELECTOR, 'div.swal-title')
    Actions_Ignore_Btn_PopUp_Text = (By.CSS_SELECTOR, 'div.swal-text')
    Actions_Ignore_Btn_PopUp_CancelBtn = (By.CSS_SELECTOR, 'button.swal-button--cancel')
    Actions_Ignore_Btn_PopUp_OkBtn = (By.CSS_SELECTOR, 'button.swal-button--confirm')
    Download_CSV_BTN = (By.CSS_SELECTOR, 'button.down_excel')
    Actions_SeeConversations_Btn = (By.CSS_SELECTOR, 'img.width-eye-img')
    Actions_AddToIntent_Btn = (By.CSS_SELECTOR, 'img.addToIntent')
    Actions_CreateIntent_Btn = (By.XPATH, "(//img[@id = 'createNewIntent'])[1]")
    Actions_SeeConversations_CustomerChat = (By.XPATH, "//h4[text() = 'Customer Chat']")
    Actions_CreateIntent_CreateIntent_PopUp = (By.CSS_SELECTOR, 'h4#exampleModalLabel')
    Create_Intent_Intent_NAME = (By.CSS_SELECTOR, 'input.input-md')
    Create_Intent_Text_Response = (By.CSS_SELECTOR, 'textarea#add_textresp')
    Create_Intent_Save_Btn = (By.CSS_SELECTOR, 'button.save_button')
    Total_Rows = (By.CSS_SELECTOR, 'tr.tr2')
    Fallback_Time = (By.XPATH, "//tbody//tr[1]/td[3]")
    Fallbacks_Value = (By.XPATH, "//tbody//tr[1]/td[4]/input")
    SelectAll_CheckBox = (By.CSS_SELECTOR, 'input#select_all')
    All_ChkBox_On_Page = (By.CSS_SELECTOR, 'input.chkbx')
    Pagination_Next_Btn = (By.CSS_SELECTOR, 'span.glyphicon-chevron-right')
    Pagination_Previous_Btn = (By.CSS_SELECTOR, 'span.glyphicon-chevron-left')
    Pagination_First_Btn = (By.XPATH, "//a[text() = 'First']")
    Pagination_Last_Btn = (By.XPATH, "//a[text() = 'Last']")



    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_ignoreBtn(self):
        self.do_click(self.Actions_Ignore_Btn)

    def get_Ignore_Btn_PopUp_Title(self):
        return self.get_element_text(self.Actions_Ignore_Btn_PopUp_Title)

    def get_Ignore_Btn_PopUp_MainText(self):
        return self.get_element_text(self.Actions_Ignore_Btn_PopUp_Text)

    def is_Ignore_Btn_PopUp_CancelBtn_visible(self):
        return self.is_visible(self.Actions_Ignore_Btn_PopUp_CancelBtn)

    def is_Ignore_Btn_PopUp_OkBtn_visible(self):
        return self.is_visible(self.Actions_Ignore_Btn_PopUp_OkBtn)

    def get_element_background_Color(self):
        self.element_mouse_hover(self.Actions_SeeConversations_Btn)
        return self.get_box_color(self.Actions_SeeConversations_Btn, 'background-color')

    def check_Customer_Chat_displayed(self):
        self.do_click(self.Actions_SeeConversations_Btn)
        return self.is_visible(self.Actions_SeeConversations_CustomerChat)

    def check_Create_Intent_PopUp_displayed(self):
        self.do_click(self.Actions_CreateIntent_Btn)

        if self.is_visible(self.Actions_CreateIntent_CreateIntent_PopUp):
            return self.get_element_text(self.Actions_CreateIntent_CreateIntent_PopUp)

    def create_new_intent(self, intent_Name, text_response):
        self.do_click(self.Actions_CreateIntent_Btn)
        self.do_send_keys(self.Create_Intent_Intent_NAME, intent_Name)
        self.do_send_keys(self.Create_Intent_Text_Response, text_response)
        self.do_click(self.Create_Intent_Save_Btn)
        return intent_Name.capitalize()

    def count_total_rows(self):
        rows = self.get_all_elements(self.Total_Rows)
        return len(rows)

    def check_delete_button_functionality(self):
        beforefallbackTime =self.get_element_text(self.Fallback_Time)
        beforefallbackValue = self.get_element_attribute(self.Fallbacks_Value, 'value')
        self.do_click(self.Actions_Ignore_Btn)
        self.do_click(self.Actions_Ignore_Btn_PopUp_OkBtn)
        time.sleep(3)
        afterfallbackTime = self.get_element_text(self.Fallback_Time)
        afterfallbackValue = self.get_element_attribute(self.Fallbacks_Value, 'value')

        if beforefallbackTime and beforefallbackValue == afterfallbackTime and afterfallbackValue:
            return False
        else:
            return True

    def check_SNo_duplicate(self):
        Rows = self.get_all_elements(self.Total_Rows)
        row_list = Rows[:]
        i = 0
        for row in Rows:
            row_list[i] = row.get_attribute('data-index')
            i = i+1
        row_set = set(row_list)

        if len(row_set) == len(row_list):
            return True
        else:
            return False

    def get_downloaded_filePath(self, file_path):
        self.do_click(self.Download_CSV_BTN)
        time.sleep(5)
        return self.is_file_exist(file_path)

    def click_select_all_checkbox_btn(self):
        self.do_click(self.SelectAll_CheckBox)

    def check_select_all_checkbox_selected(self):
        return self.elements_are_selected(self.All_ChkBox_On_Page, self.SelectAll_CheckBox)

    def click_pagination_next_button(self):
        if self.count_total_rows() > 10:
            self.do_click(self.Pagination_Next_Btn)
            rows = self.get_all_elements(self.Total_Rows)
            for row in rows:
                if row.get_attribute('data-index') == '11' and row.get_attribute('style') == '':
                    return True


    def click_pagination_previous_button(self):
        if self.count_total_rows() > 10:
            self.do_click(self.Pagination_Next_Btn)
            self.do_click(self.Pagination_Previous_Btn)
            rows = self.get_all_elements(self.Total_Rows)
            for row in rows:
                if row.get_attribute('data-index') == '1' and row.get_attribute('style') == '':
                    return True

    def click_pagination_first_button(self):
        total_rows = self.count_total_rows()
        self.do_click(self.Pagination_Last_Btn)
        self.do_click(self.Pagination_First_Btn)
        rows = self.get_all_elements(self.Total_Rows)
        first_row = rows[0]
        if first_row.get_attribute('data-index') == '1':
            return True
        else:
            return False

    def click_pagination_Last_button(self):
        total_rows = self.count_total_rows()
        self.do_click(self.Pagination_Last_Btn)
        rows = self.get_all_elements(self.Total_Rows)
        last_row = rows[-1]
        if last_row.get_attribute('data-index') == str(total_rows):
            return True
        else:
            return False





