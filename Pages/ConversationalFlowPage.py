from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ConversationalFlowPage(BasePage):
    """By Locators"""
    Page_header = (By.CSS_SELECTOR, 'h1.main-title2')
    Create_Node_Dropdown_Btn = (By.XPATH, "//a[@title='Create Node']")
    Create_Node_Dropdown_Box = (By.XPATH, "//li//a[@title='Create Node']/following-sibling::ul")
    LOAD_SAVED_DATA = (By.CSS_SELECTOR, 'a#load_local')
    JSON_Btn = (By.CSS_SELECTOR, 'a#get_data')
    JSON_Representation_Head_Text = (By.XPATH, "//label[text() ='JSON Representation']")
    All_Nodes = (By.CSS_SELECTOR, 'div.flowchart-operator-inputs')
    Delete_Btn = (By.CSS_SELECTOR, 'a.delete_selected_button')
    Delete_Btn_PopUp_Head_Text = (
    By.XPATH, "//div[text() = 'Once deleted, you will not be able to recover this  node.']")
    Node_To_Be_Deleted = (By.XPATH, "(//div[@class = 'flowchart-operator-inputs']/following-sibling::div[1])[1]")
    Delete_PopUp_OK_Btn = (By.CSS_SELECTOR, 'button.swal-button--confirm')

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self):
        if self.is_visible(self.Page_header):
            return self.get_element_text(self.Page_header)

    def click_create_node_dropdown_btn(self):
        self.do_click(self.Create_Node_Dropdown_Btn)
        return self.is_visible(self.Create_Node_Dropdown_Box)

    def click_load_saved_data_btn(self):
        return self.is_clickable(self.LOAD_SAVED_DATA)

    def click_json_btn(self):
        self.do_click(self.JSON_Btn)
        return self.is_visible(self.JSON_Representation_Head_Text)

    def click_delete_btn(self):
        all_Nodes = self.get_all_elements(self.All_Nodes)
        for node in all_Nodes:
            node.click()
            break
        node_text = self.get_element_text(self.Node_To_Be_Deleted)
        print(node_text)
        self.do_click(self.Delete_Btn)
        self.do_click(self.Delete_PopUp_OK_Btn)
        node_text1 = self.get_element_text(self.Node_To_Be_Deleted)
        print(node_text1)
        if node_text != node_text1:
            return True
        else:
            return False
