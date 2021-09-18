from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_RegistrationPage(BaseTest):

    def test_allElements_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        flag = self.registrationPage.is_allelements_visible()
        assert flag

    def test_placeholder_text(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        assert self.registrationPage.get_placeholder_attribute_value('placeholder') == TestData.PLACEHOLDER_ATT_VALUES

    def test_OTPfield_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        assert self.registrationPage.is_OTPfield_visible(TestData.RgstPageEle) == True

    def test_registerHere_link(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        assert self.registrationPage.is_header_visible() == True

    def test_mobileNumber_10Digit_Validation(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()

        self.registrationPage.enter_phoneNumber_invalid(TestDataFromExcel.NINE_DIGIT_MOBILE_NUMBER)
        NineDigitMobRes = self.registrationPage.is_invalidPhone_visible()

        self.registrationPage.enter_phoneNumber_invalid(TestDataFromExcel.ELEVEN_DIGIT_MOBILE_NUMBER)
        ElevenDigitMobRes = self.registrationPage.is_invalidPhone_visible()

        assert NineDigitMobRes == ElevenDigitMobRes == True

    def test_mobileNumber_spclChar_alphabets_Validation(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()

        self.registrationPage.enter_phoneNumber_invalid(TestDataFromExcel.SPECIAL_CHAR_MOBILE_NUMBER)
        SpclCharMobRes = self.registrationPage.is_invalidPhone_visible()

        self.registrationPage.enter_phoneNumber_invalid(TestDataFromExcel.ALPHANUM_MOBILE_NUMBER)
        AlphaNumMobRes = self.registrationPage.is_invalidPhone_visible()

        assert SpclCharMobRes == AlphaNumMobRes == True

    def test_invalid_password_lessThan8_Validations(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        self.registrationPage.enter_password_invalid(TestDataFromExcel.INV_PWD_LESS_THAN_EIGHT)
        LessThanEIGHTRes = self.registrationPage.is_invalidPWD_visible()
        assert LessThanEIGHTRes == True

    def test_invalid_password_noLowerCase_Validations(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        self.registrationPage.enter_password_invalid(TestDataFromExcel.INV_PWD_NO_LWRCASE)
        NoLwrCaseRes = self.registrationPage.is_invalidPWD_visible()
        assert NoLwrCaseRes == True

    def test_invalid_password_noUpperCase_Validations(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        self.registrationPage.enter_password_invalid(TestDataFromExcel.INV_PWD_NO_UPPRCASE)
        NoUpprCaseRes = self.registrationPage.is_invalidPWD_visible()
        assert NoUpprCaseRes == True

    def test_invalid_password_noSpecialChar_Validations(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        self.registrationPage.enter_password_invalid(TestDataFromExcel.INV_PWD_NO_SPCLCHAR)
        NoSpclCharRes = self.registrationPage.is_invalidPWD_visible()
        assert NoSpclCharRes == True

    def test_invalid_password_noNumbers_Validations(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        self.registrationPage.enter_password_invalid(TestDataFromExcel.INV_PWD_NO_NUMBER)
        NoNumRes = self.registrationPage.is_invalidPWD_visible()
        assert NoNumRes == True

    def test_invalid_username_noSpecialChar_Validations(self):
        self.loginPage = LoginPage(self.driver)
        self.registrationPage = self.loginPage.click_RegisterHere_link()
        self.registrationPage.enter_invalid_username(TestDataFromExcel.INV_UNAME_SPECIAL_CHAR)
        specialChar = self.registrationPage.is_invalid_username_visible()
        assert specialChar == True

