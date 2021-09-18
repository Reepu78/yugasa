import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.ChangePasswordPage import ChangePasswordPage


class EditProfilePage(BasePage):
    """By Locators"""
    EditProfile_Btn = (By.CSS_SELECTOR, 'button.editProfileTab')
    ChangePwd_Btn = (By.CSS_SELECTOR, 'button.chngPswrdTab')
    EditProfile_box = (By.CSS_SELECTOR, 'div.edit-profile-box')
    CompanyName = (By.NAME, 'name')
    EmailId = (By.ID, 'email-Id')
    SubmitBtn = (By.CSS_SELECTOR, 'button.confirm-btn')
    Change_Password_Submit_Btn = (By.CSS_SELECTOR, 'button#submitBtn')
    Profile_Photo = (By.ID, 'upload')

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)


    def is_editProfilePage_visible(self):
        editProfileBtn_visible = self.is_visible(self.EditProfile_Btn)
        chngPwdBtn_visible = self.is_visible(self.ChangePwd_Btn)
        editProfileBox_visible = self.is_visible(self.EditProfile_box)

        EditProfilePage_elements = [editProfileBtn_visible, chngPwdBtn_visible, editProfileBox_visible]
        return EditProfilePage_elements

    def change_companyName(self, editCompName):
        self.clear_element(self.CompanyName)
        self.do_send_keys(self.CompanyName, editCompName)
        self.do_click(self.SubmitBtn)
        time.sleep(3)
        self.driver.switch_to.alert.accept()

    def get_CompanyName_ValueAttribute_val(self, attName):
        return self.get_element_attribute(self.CompanyName, attName)

    def isCompanyName_enabled(self):
        return self.is_element_enable(self.CompanyName)

    def isEmailId_enabled(self):
        return self.is_element_enable(self.EmailId)

    def click_changePwdBtn(self):
        self.do_click(self.ChangePwd_Btn)
        return ChangePasswordPage(self.driver)

    def click_changePwd_submitBtn(self):
        self.do_click(self.Change_Password_Submit_Btn)

    def upload_file(self, filePath):
        self.do_send_keys(self.Profile_Photo, filePath)
        self.do_click(self.SubmitBtn)
        alert_text = self.get_alert_text()
        self.accept_alert()
        return alert_text

