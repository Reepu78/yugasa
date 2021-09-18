from Config.TestData import TestData
from TestData.ExcelLogic import TestDataFromExcel
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_BotSettingsPage(BaseTest):

    def test_bot_setting_page_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.bot_settings_elements_displayed() == True

    def test_elements_design_tab(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_elementsin_design_tab() == True

    def test_changeColor_dropdown_displayed(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_changecolor_dropdown_visible() == True

    def test_color_picker_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        self.botSettingsPage.choose_color_picker('255','0','0', id = 'headBgColor')
        assert self.botSettingsPage.click_save_button()== TestData.DESIGN_TAB_SUCCESS_ALERT_TEXT

    def test_head_background_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.head_background_change_color('255', '0', '0') == TestData.RED_COLOR

    def test_head_text_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_head_text_color('4', '0', '255') == TestData.BLUE_COLOR

    def test_close_button_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_close_button_color('4', '0', '255') == TestData.BLUE_COLOR

    def test_chat_bot_speech_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_speech_color('255', '0', '247') == TestData.PINK_COLOR

    def test_chat_bot_text_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_text_color('89', '255', '0') == TestData.GREEN_COLOR


    def test_chatbot_user_speech_bubble_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_user_speech_bubble_color('255', '0', '0') == TestData.RED_COLOR

    def test_chatbot_user_text_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_user_text_color('255', '0', '247') == TestData.PINK_COLOR

    def test_chatbot_border_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_border_color('255', '136', '0') == TestData.ORANGE_COLOR

    def test_chatbot_window_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_window_color('255', '136', '0') == TestData.ORANGE_COLOR

    def test_chatbot_send_btn_color_functionality(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.check_chat_bot_send_btn_color('255', '0', '0') == TestData.RED_COLOR

    def test_integration_Options_display(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.get_integration_options() == TestData.INTEGRATION_OPTIONS

    def test_online_status_on_chatbot(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.get_tag_line_text_chatbot() == 'Yugasa Bot'

    def test_bot_Setting_click(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        assert self.botSettingsPage.click_bot_code()

    def test_communications(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestDataFromExcel.USERNAME, TestDataFromExcel.readPassword(self))
        self.botSettingsPage = self.homePage.click_bot_settings_link()
        self.botSettingsPage.add_communications()

