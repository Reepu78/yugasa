import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.TestData import TestData
from Pages.BasePage import BasePage


class CommunicationPage(BasePage):

    """By Locators"""
    Head_Title = (By.CSS_SELECTOR, 'h1.main-title')
    Download_CSV_Btn = (By.CSS_SELECTOR, 'button.down_excel')
    Total_Rows = (By.CSS_SELECTOR, 'tr.tr2')
    Calendar_Date_Range = (By.CSS_SELECTOR, 'input#dateRange')
    Left_Month_Year_Value = (By.XPATH, "(//th[@class= 'month'])[1]")
    Right_Month_Year_Value = (By.XPATH, "(//th[@class= 'month'])[2]")
    Calendar_Next_Btn = (By.CSS_SELECTOR, 'th.next.available')
    Calendar_Back_BTN = (By.CSS_SELECTOR, "th.prev.available")
    Calendar_Apply_Btn = (By.CSS_SELECTOR, 'button.applyBtn')
    Calendar_Date_Range_Display = (By.CSS_SELECTOR, 'span.drp-selected')
    Calendar_Left_Day = (By.XPATH, "//div[@class='drp-calendar left'] //td[@class ='available' or @ class ='weekend "
                                   "available' or @ class ='active start-date active end-date available' or @ class "
                                   "='in-range available' or @ class ='weekend in-range available']")

    Calendar_Right_Day = (By.XPATH, "//div[@class='drp-calendar right']// td[@class ='available' or @ class ='weekend "
                                    "available' or @ class ='active start-date active end-date available' or @ class "
                                    "='in-range available' or @ class ='weekend in-range available']")

    SelectAll_CheckBox = (By.CSS_SELECTOR, "input.chkall")
    All_ChkBox_On_Page = (By.CSS_SELECTOR, 'input.chkbx')
    Action_Edit_Button = (By.XPATH, "(//p[@title = 'Edit'])[1]")
    Action_Update_Button = (By.CSS_SELECTOR, "button.btn-update")
    Action_Cancel_Button = (By.XPATH, "//button[text() = 'Cancel']")
    Action_View_Button = (By.XPATH, "(//button[@class = 'btn btn-primary btn-xs user'])[1]")
    View_Customer_Chat_Window = (By.XPATH, "(//h4[@class = 'modal-title'])[1]")
    Status_Dropdown = (By.XPATH, "(//select[@id = 'gender1'])[1]")
    Status_DropDown_Values = (By.XPATH, "(//select[@id = 'gender1'])[1]/option")
    Edit_EmailID_txtfield = (By.XPATH, "(//input[@id = 'email'])[1]")
    Edit_Phone_txtfield = (By.XPATH, "(//input[@id = 'phone'])[1]")
    EmailId = (By.XPATH, "//tbody//tr[1]//td[6]")
    Phone = (By.XPATH, "//tbody//tr[1]//td[7]")
    Delete_Btn = (By.XPATH, "(//p[@title = 'Delete'])[1]")
    Delete_popup_OK_Btn = (By.CSS_SELECTOR, 'button.swal-button--danger')
    Row_to_be_Deleted = (By.XPATH, "(//tbody//tr[1])[1]")
    Filter_Leads_DropDown = (By.ID, 'filterLeads')
    All_Action_View_Button = (By.CSS_SELECTOR, 'button.btn.btn-primary.btn-xs.user')
    Customer_Chats = (By.XPATH, "//div[@class = 'table_chat']/div")
    All_Customer_Chat_Close_Btn = (By.XPATH, "(//button[@class = 'modal_close'])")
    Pagination_Next_Btn = (By.CSS_SELECTOR, 'span.glyphicon-chevron-right')
    Pagination_Previous_Btn = (By.CSS_SELECTOR, 'span.glyphicon-chevron-left')
    Pagination_First_Btn = (By.XPATH, "//a[text() = 'First']")
    Pagination_Last_Btn = (By.XPATH, "//a[text() = 'Last']")



    """Page Actions"""

    def __init__(self, driver):
        super().__init__(driver)

    def is_headTitle_visble(self):
        return self.is_visible(self.Head_Title)

    def get_downloaded_filePath(self, file_path):
        self.do_click(self.Download_CSV_Btn)
        time.sleep(5)
        return self.is_file_exist(file_path)

    def click_calendarDateRange(self):
        self.do_click(self.Calendar_Date_Range)

    def click_select_all_checkbox_btn(self):
        self.do_click(self.SelectAll_CheckBox)

    def select_Leads_Dropdown(self):
        select = Select(self.get_element(self.Filter_Leads_DropDown))
        select.select_by_value('Leads')

    def check_select_all_checkbox_selected(self):
        return self.elements_are_selected(self.All_ChkBox_On_Page, self.SelectAll_CheckBox)

    def check_edit_elements(self):
        self.do_click(self.Action_Edit_Button)
        return self.is_visible(self.Action_Update_Button)

    def check_update_btn(self, emailText, phoneText):
        self.do_click(self.Action_Edit_Button)
        self.driver.find_element_by_xpath("(//input[@id = 'email'])[1]").clear()
        self.do_send_keys(self.Edit_EmailID_txtfield, emailText)
        self.driver.find_element_by_xpath("(//input[@id = 'phone'])[1]").clear()
        self.do_send_keys(self.Edit_Phone_txtfield, phoneText)
        self.do_click(self.Action_Update_Button)
        time.sleep(2)
        emailVal = self.get_element_text(self.EmailId)
        phoneVal = self.get_element_text(self.Phone)
        return [emailVal, phoneVal]

    def get_Name_in_row(self):
        return self.get_element_attribute(self.Row_to_be_Deleted, 'data-email')

    def delete_record_get_name(self):
        # beforeDeletionRows = self.count_total_rows()
        self.do_click(self.Delete_Btn)
        self.do_click(self.Delete_popup_OK_Btn)
        time.sleep(3)
        # afterDeletionRows = self.count_total_rows()

        # if beforeDeletionRows != afterDeletionRows:
        return self.get_element_attribute(self.Row_to_be_Deleted, 'data-email')
        # else:
        #     return False


    def click_cancel_btn(self):
        self.do_click(self.Action_Edit_Button)
        if self.is_visible(self.Action_Update_Button):
            self.do_click(self.Action_Cancel_Button)
            time.sleep(1)
            return self.is_visible(self.Action_Edit_Button)

    def count_total_rows(self):
        Rows = self.get_all_elements(self.Total_Rows)
        return len(Rows)

    def date_picker_functionality(self, Expected_Left_Date,Expected_Right_Date):
        self.click_calendarDateRange()
        self.select_dates_in_calendar(Expected_Left_Date,Expected_Right_Date)
        self.do_click(self.Calendar_Apply_Btn)
        self.click_calendarDateRange()
        Date_Display =self.get_element_text(self.Calendar_Date_Range_Display)
        Left_Date = Date_Display.split("-")[0].strip()
        Right_Date = Date_Display.split("-")[1].strip()
        Left_Day = Left_Date.split("/")[0]
        Right_Day = Right_Date.split("/")[0]
        Expected_Left_Day = Expected_Left_Date.split(" ")[0].strip()
        Expected_Right_Day = Expected_Right_Date.split(" ")[0].strip()
        if Left_Day==Expected_Left_Day and Right_Day==Expected_Right_Day:
            return True
        else:
            return False

    def click_view_button(self):
        self.do_click(self.Action_View_Button)
        return self.is_element_displayed(self.View_Customer_Chat_Window)

    def check_status_dropdown_values(self):
        self.do_click(self.Action_Edit_Button)
        self.do_click(self.Status_Dropdown)
        status_dropdown_values = self.select_by_dropdown(self.Status_Dropdown)
        return status_dropdown_values

    def select_status_dropdown_values(self, Status_Value):
        self.do_click(self.Action_Edit_Button)
        self.do_click(self.Status_Dropdown)
        select = Select(self.get_element(self.Status_Dropdown))
        select.select_by_visible_text(Status_Value)
        self.do_click(self.Action_Update_Button)
        elements = self.get_all_elements(self.Status_DropDown_Values)
        for ele in elements:
            if ele.text == Status_Value:
                return self.is_element_displayed(ele.get_attribute('style'))

    def get_total_customer_chats(self):
        All_View_Buttons = self.get_all_elements(self.All_Action_View_Button)

        if len(All_View_Buttons) > 10:
            i = 1
            for view_button in All_View_Buttons:
                if view_button.is_displayed():
                    view_button.click()
                    time.sleep(1)
                    len_customer_chats = len(self.get_all_elements(self.Customer_Chats))
                    self.driver.find_element_by_xpath("(//button[text() = '×'])["+str(i)+"]").click()
                    i = i+2
                    time.sleep(1)
                else:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)
                    self.driver.find_element_by_css_selector("span.glyphicon.glyphicon-chevron-right").click()
                    view_button.click()
                    time.sleep(1)
                    len_customer_chats = len(self.get_all_elements(self.Customer_Chats))
                    self.driver.find_element_by_xpath("(//button[text() = '×'])[" + str(i) + "]").click()
                    i = i + 2
                    time.sleep(1)
            return len_customer_chats

        else:
            i = 1
            for view_button in All_View_Buttons:
                view_button.click()

                time.sleep(1)
                len_customer_chats = len(self.get_all_elements(self.Customer_Chats))
                self.driver.find_element_by_xpath("(//button[text() = '×'])[" + str(i) + "]").click()
                i = i + 2
                time.sleep(1)
            return len_customer_chats


    def click_pagination_next_button(self):
        if self.count_total_rows() > 10:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            self.do_click(self.Pagination_Next_Btn)
            rows = self.get_all_elements(self.Total_Rows)
            for row in rows:
                if row.get_attribute('data-index') == '11' and row.get_attribute('style') == '':
                    return True


    def click_pagination_previous_button(self):
        if self.count_total_rows() > 10:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            self.do_click(self.Pagination_Next_Btn)
            self.do_click(self.Pagination_Previous_Btn)
            rows = self.get_all_elements(self.Total_Rows)
            for row in rows:
                if row.get_attribute('data-index') == '1' and row.get_attribute('style') == '':
                    return True

    def click_pagination_first_button(self):
        total_rows = self.count_total_rows()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
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
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.do_click(self.Pagination_Last_Btn)
        rows = self.get_all_elements(self.Total_Rows)
        last_row = rows[-1]
        if last_row.get_attribute('data-index') == str(total_rows):
            return True
        else:
            return False

































