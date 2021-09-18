import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class RegistrationPage(BasePage):
    """By Locators"""
    Header = (By.XPATH, "//h3[contains(text(), 'REGISTER')]")
    Username = (By.ID, "username")
    INV_Username = (By.XPATH, "//input[@id = 'username' and @aria-invalid='true']")
    EmailId = (By.ID, "email-Id")
    Password = (By.ID, "password")
    INV_PWD = (By.XPATH, '//input[@id = "password" and @aria-invalid="true"]')
    Phone = (By.ID, "phone")
    Inv_Phone = (By.XPATH, '//input[@id = "phone" and @aria-invalid="true"]')
    Send_OTP_Button = (By.CSS_SELECTOR, 'button.resendbtn.SendOTP')
    OTP = (By.CSS_SELECTOR, "input.otpField")
    ResendOTPBtn = (By.CSS_SELECTOR, "button.resendbtn.otpresend")
    URLField = (By.ID, "websiteUrl")
    TermsCondLink = (By.CSS_SELECTOR, "h5.tnc_btn")
    TermsCondCheckBox = (By.NAME, "trms_cndtn_chkbx")
    SignUpBtn = (By.ID, "submitBtn")
    LoginHereLink = (By.LINK_TEXT, "Login Here")
    ForgotPasswordLink = (By.LINK_TEXT, "Forgot Password")
    Password_Eye_Btn = (By.CSS_SELECTOR, 'span.fa-eye-slash')
    Accept_Cookies = (By.XPATH, "//a[@id = 'hs-eu-confirmation-button']")

    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)

    def is_allelements_visible(self):
        return self.is_visible(self.Header) and self.is_visible(self.Username) and self.is_visible(
            self.EmailId) and self.is_visible(self.Password) and self.is_visible(self.Phone) and self.is_visible(
            self.URLField) and self.is_visible(self.TermsCondCheckBox) and self.is_visible(
            self.TermsCondLink) and self.is_visible(self.SignUpBtn) and self.is_visible(
            self.LoginHereLink) and self.is_visible(self.ForgotPasswordLink)

    def is_header_visible(self):
        return self.is_visible(self.Header)

    def get_placeholder_attribute_value(self, attName):
        att_uname_val = self.get_element_attribute(self.Username, attName)
        att_password_val = self.get_element_attribute(self.Password, attName)
        att_emailID_val = self.get_element_attribute(self.EmailId, attName)
        att_url_val = self.get_element_attribute(self.URLField, attName)
        att_phone_val = self.get_element_attribute(self.Phone, attName)

        placeholder_val = [att_uname_val, att_emailID_val, att_password_val, att_phone_val, att_url_val]
        return placeholder_val

    def is_OTPfield_visible(self, RgstPageEle):
        self.do_send_keys(self.Username, RgstPageEle[0])
        self.do_send_keys(self.EmailId, RgstPageEle[1])
        self.do_send_keys(self.Password, RgstPageEle[2])
        self.do_send_keys(self.Phone, RgstPageEle[3])
        self.do_send_keys(self.URLField, RgstPageEle[4])
        self.do_click(self.Send_OTP_Button)
        return self.is_element_displayed(self.OTP)

    def enter_phoneNumber_invalid(self, invMobNum):
        self.do_send_keys(self.Phone, invMobNum)
        self.do_click(self.Header)

    def is_invalidPhone_visible(self):
        return self.is_element_displayed(self.Inv_Phone)

    def enter_password_invalid(self, invPwd):
        if self.is_element_displayed(self.Accept_Cookies):
            self.do_click(self.Accept_Cookies)
            self.clear_element(self.Password)
            self.do_send_keys(self.Password, invPwd)
            time.sleep(2)
            self.do_click(self.Header)
        else:
            self.clear_element(self.Password)
            self.do_send_keys(self.Password, invPwd)
            time.sleep(2)
            self.do_click(self.Header)

    def is_invalidPWD_visible(self):
        return self.is_element_displayed(self.INV_PWD)
        # self.driver.refresh()
        # time.sleep(3)

    def get_element_cssProperty(self, elementName, elementVal, cssProperty):
        self.do_send_keys(elementName, elementVal)
        self.do_click(self.Header)
        return self.get_box_color(elementName, cssProperty)

    def enter_invalid_username(self, inv_uname):
        if self.is_element_displayed(self.Accept_Cookies):
            self.do_click(self.Accept_Cookies)
            self.clear_element(self.Username)
            self.do_send_keys(self.Username, inv_uname)
            time.sleep(2)
            self.do_click(self.Header)
        else:
            self.clear_element(self.Username)
            self.do_send_keys(self.Username, inv_uname)
            time.sleep(2)
            self.do_click(self.Header)

    def is_invalid_username_visible(self):
        return self.is_element_displayed(self.INV_Username)

