


import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.color import Color

from Config.TestData import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BotSettingsPage(BasePage):
    """By Locator"""
    Head_Title = (By.CSS_SELECTOR, 'h1.main-title2')
    Bot_Settings_All_Tabs = (By.XPATH, "//div[@class = 'tab']//button")
    Chatbot = (By.CSS_SELECTOR, 'div#botBorder')
    DesignTab_All_Fields = (By.CSS_SELECTOR, 'p.pLabel')
    ChangeColor_DropDown = (By.NAME, 'my-select')
    Color_Picker = (By.XPATH, "//h4//input[@id]")
    Save_Btn = (By.CSS_SELECTOR, 'button.bot_save')
    Online_Status_TxtField = (By.CSS_SELECTOR, 'input#source1')
    Preview_URL = (By.CSS_SELECTOR, 'input#websiteUrl')
    Preview_Btn = (By.XPATH, "(//div[@class = 'prev-btn'])[1]")
    NewWindow_Chat_Icon = (By.CSS_SELECTOR, 'div.hy-icon')
    NewWindow_Chat_Icon_Tag_Line = (By.XPATH, "//p[@class='tag-line']")
    NewWindow_ChatBot_Frame = (By.XPATH, "//iframe[@id = 'frame-lode']")
    NewWindow_ChatBot_Header = (By.CSS_SELECTOR, 'div.contact-profile')
    NewWindow_ChatBot_Close_Btn = (By.XPATH, '//div[@class="close-img"]/*[local-name()="svg"][@focusable="false"]')
    NewWindow_ChatBot_Text = (By.XPATH, "(//li[@class='sent']/p)[1]")
    NewWindow_ChatBot_User_Text_Field = (By.ID, 'msg')
    NewWindow_ChatBot_User_Text_Send_Btn = (By.XPATH, "//button[@class = 'submit']/*[local-name()= 'svg']")
    NewWindow_ChatBot_Send_Btn_Background = (By.XPATH, "//button[@type='submit']")
    NewWindow_ChatBot_User_Text = (By.XPATH, "(//li[@class = 'replies']/p)[1]")
    NewWindow_ChatBot_Border = (By.XPATH, "//*[@id='iframe-box']")
    NewWindow_ChatBot_Window = (By.ID, 'frame')
    Code_Snippet = (By.CSS_SELECTOR, 'textarea.css-file')
    Integrations_Options = (By.XPATH, "((//div[@class = 'col-lg-12'])[10]/div/div//h3)")



    """Page Actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.second_driver = None

    def bot_settings_elements_displayed(self):
        allTabs = self.get_all_elements(self.Bot_Settings_All_Tabs)
        tabs_text = allTabs[:]
        i = 0
        for tab in allTabs:
            tabs_text[i] = tab.text
            i = i + 1

        if tabs_text == ['Design', 'Bot Code', 'Integrations', 'Subscription']:
            return self.is_element_displayed(self.Chatbot)

    def check_elementsin_design_tab(self):
        elements = self.get_all_elements(self.DesignTab_All_Fields)
        fields_text = elements[:]
        i = 0
        for element in elements:
            fields_text[i] = element.text
            i = i + 1

        if fields_text == ['Change Color:', 'Online Status:', 'Upload Logo:', 'Preview:']:
            return True

    def check_changecolor_dropdown_visible(self):
        return self.is_element_displayed(self.ChangeColor_DropDown)

    def choose_color_picker(self, R, G, B, id):
        actions = ActionChains(self.driver)
        colorPickerElements = self.get_all_elements(self.Color_Picker)
        for color in colorPickerElements:
            if color.get_attribute("id") == id:
                color.click()

                N = 3  # number of times you want to press TAB

                for _ in range(N):
                    actions = actions.send_keys(Keys.TAB)
                actions.send_keys(R)

                actions = actions.send_keys(Keys.TAB)
                actions.send_keys(G)

                actions = actions.send_keys(Keys.TAB)
                actions.send_keys(B)

                actions.send_keys(Keys.ENTER)
                actions.perform()

    def click_save_button(self):
        self.do_click(self.Save_Btn)
        alert_text = self.get_alert_text()
        self.accept_alert()
        return alert_text

    def get_tag_line_text_chatbot(self):
        self.clear_element(self.Online_Status_TxtField)
        self.do_send_keys(self.Online_Status_TxtField, 'Yugasa Bot')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        text = self.get_element_text(self.NewWindow_Chat_Icon_Tag_Line)
        return text

    def head_background_change_color(self, R,G,B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('Head Background color')
        self.choose_color_picker(R,G,B,'headBgColor')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        color = self.get_box_color(self.NewWindow_ChatBot_Header, 'background')
        rgb = color.split(" n")[0]
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return rgb

    def check_head_text_color(self, R,G,B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('Head Text Color')
        self.choose_color_picker(R, G, B, 'headText_color')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        color_RGBA = Color.from_string(self.get_box_color(self.NewWindow_Chat_Icon_Tag_Line, 'color'))
        # color_RGBA = self.get_box_color(self.NewWindow_Chat_Icon_Tag_Line, 'color')
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        # return color_RGBA.rgb
            return color_RGBA.rgb

    def check_close_button_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('Close Button Color')
        self.choose_color_picker(R, G, B, 'cross_head_color')
        self.click_save_button()
        self.do_send_keys(self.Preview_URL, 'https://helloyubo.com/')
        self.do_click(self.Preview_Btn)
        if len(self.driver.window_handles) == 2:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.do_click(self.NewWindow_Chat_Icon)
            color =self.get_box_color(self.NewWindow_ChatBot_Close_Btn, 'fill')
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            return color

    def check_chat_bot_speech_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('ChatBot Speech Bubble Color')
        self.choose_color_picker(R, G, B, 'botwidgetbgcolor')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        color = self.get_box_color(self.NewWindow_ChatBot_Text, 'background')
        rgb = color.split(" n")[0]
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return rgb

    def check_chat_bot_text_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('ChatBot Text Color')
        self.choose_color_picker(R, G, B, 'bottext_head')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        color_RGBA = Color.from_string(self.get_box_color(self.NewWindow_ChatBot_Text, 'color'))
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return color_RGBA.rgb

    def check_chat_bot_user_speech_bubble_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('User Speech Bubble Color')
        self.choose_color_picker(R, G, B, 'userBg_head')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        self.do_send_keys(self.NewWindow_ChatBot_User_Text_Field, 'Hi')
        time.sleep(1)
        self.do_click(self.NewWindow_ChatBot_User_Text_Send_Btn)
        color = self.get_box_color(self.NewWindow_ChatBot_User_Text, 'background')
        rgb = color.split(" n")[0]
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return rgb

    def check_chat_bot_user_text_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('User Text Color')
        self.choose_color_picker(R, G, B, 'usertext_head')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        self.do_send_keys(self.NewWindow_ChatBot_User_Text_Field, 'Hi')
        time.sleep(1)
        self.do_click(self.NewWindow_ChatBot_User_Text_Send_Btn)
        color_RGBA = Color.from_string(self.get_box_color(self.NewWindow_ChatBot_User_Text, 'color'))
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return color_RGBA.rgb

    def check_chat_bot_border_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('Chatbot Border Color')
        self.choose_color_picker(R, G, B, 'botBorder_color')
        self.click_save_button()
        self.do_send_keys(self.Preview_URL, 'https://helloyubo.com/')
        self.do_click(self.Preview_Btn)
        if len(self.driver.window_handles) == 2:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.do_click(self.NewWindow_Chat_Icon)
        color= self.get_box_color(self.NewWindow_ChatBot_Border, 'border')
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return color.split("solid ")[-1]


    def check_chat_bot_window_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('Chat Window Color')
        self.choose_color_picker(R, G, B, 'chatScreen_color')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        color= self.get_box_color(self.NewWindow_ChatBot_Window, 'background')
        rgb = color.split(" n")[0]
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return rgb

    def check_chat_bot_send_btn_color(self, R, G, B):
        select = Select(self.get_element(self.ChangeColor_DropDown))
        select.select_by_visible_text('Icon Background Color')
        self.choose_color_picker(R, G, B, 'iconBg_color')
        self.click_save_button()
        self.click_preview_button(url='https://helloyubo.com/')
        color= self.get_box_color(self.NewWindow_ChatBot_Send_Btn_Background, 'background')
        rgb = color.split(" n")[0]
        if len(self.driver.window_handles)>1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        return rgb

    def click_preview_button(self,url):
        self.do_send_keys(self.Preview_URL, url)
        self.do_click(self.Preview_Btn)
        if len(self.driver.window_handles) == 2:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)
            self.do_hard_refresh()
            self.do_click(self.NewWindow_Chat_Icon)
            frame = self.get_element(self.NewWindow_ChatBot_Frame)
            self.driver.switch_to.frame(frame)

    def click_bot_code(self):
        tabs = self.get_all_elements(self.Bot_Settings_All_Tabs)
        for tab in tabs:
            if tab.text == 'Bot Code':
                tab.click()
                text = self.get_element_text(self.Code_Snippet).split("<")
                if text[1].strip()== "link rel=\"stylesheet\" href=\"https://yubo.yugasa.org/assets/Testyubo.bot.css\">":
                    if text[2].strip() == "script src=\"https://yubo.yugasa.org/assets/Testyubo.bot.js\">":
                        if text[3].strip()== "/script>":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

    def get_integration_options(self):
        tabs = self.get_all_elements(self.Bot_Settings_All_Tabs)
        for tab in tabs:
            if tab.text == 'Integrations':
                tab.click()
                integrations = self.get_all_elements(self.Integrations_Options)
                intOptionsText = integrations[:]
                i=0
                for intOption in integrations:
                    intOptionsText[i] = intOption.text
                    i=i+1

                return intOptionsText

    # def add_communications(self):
    #     self.click_preview_button(url='https://helloyubo.com/')
    #     self.do_send_keys(self.NewWindow_ChatBot_User_Text_Field, 'Hi')
    #     time.sleep(1)
    #     self.do_click(self.NewWindow_ChatBot_User_Text_Send_Btn)
    #     bot_URL = self.driver.current_url
    #
    #     second_driver = webdriver.Chrome(executable_path="/Users/tshas/AutomationScenes/WebDrivers/ChromeDriver/chromedriver")
    #     second_driver.get(bot_URL)
    #     second_driver.maximize_window()
    #     second_driver.find_element_by_css_selector("div.hy-icon").click()
    #     time.sleep(2)
    #     frame = second_driver.find_element_by_xpath("//iframe[@id = 'frame-lode']")
    #     second_driver.switch_to.frame(frame)
    #     print("I am inside the frame")
    #     i = 0
    #     while len(TestData.COMMUNICATION_CHAT)<16:
    #         second_driver.find_element_by_id('msg').send_keys(TestData.COMMUNICATION_CHAT[i])
    #         time.sleep(1)
    #         second_driver.find_element_by_xpath("//button[@class = 'submit']/*[local-name()= 'svg']").click()
    #         i= i+1
    #         time.sleep(2)
    #     # self.do_click(self.NewWindow_ChatBot_User_Text_Send_Btn)




    



 













