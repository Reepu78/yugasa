import time

import requests
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.BotSettingsPage import BotSettingsPage
from Pages.CommunicationPage import CommunicationPage
from Pages.ConversationalFlowPage import ConversationalFlowPage
from Pages.CreateIntentPage import CreateIntentPage
from Pages.EditProfilePage import EditProfilePage
from Pages.FallbacksPage import FallbacksPage
from Pages.HelpPage import HelpPage
from Pages.IntegrationsPage import IntegrationsPage
from Pages.SlotsPage import SlotsPage
from Pages.VisitorsLog import VisitorsLog
from Pages.WebhooksAndActions import WebhooksAndActions
from Pages.YourStoryPage import YourStoryPage


class HomePage(BasePage):
    """Page Objects"""
    # Logo_HomePage = (By.XPATH, "//a[@class = 'logo']")
    Logo_HomePage = (By.CLASS_NAME, "logo")
    Dashboard_LeftMenu = (By.XPATH, "//a[@href = '/adminPanel']")
    SignOut_LeftMenu = (By.XPATH, "(//a[@href= '/logOut'])[2]")
    EditProfile_LeftMenu = (By.XPATH, "(//a[@href= '/editProfile'])[2]")
    All_Links = (By.XPATH, "//a[@href]")
    Calendar_Range = (By.CSS_SELECTOR, 'input#dateRange')
    Total_Conversation = (By.XPATH, "//p[text() = 'Total Conversation']")
    Number_Total_Conversation = (By.XPATH, "(//h3[@id = 'totalConversation'])[1]")
    Visitors_Log_Link = (By.XPATH, "//a[@href= '/logs']")
    No_of_Visitors = (By.XPATH, "//p[text() = 'No. of Visitors']")
    Number_No_of_Visitors = (By.XPATH, "(//h3[@id = 'totalConversation'])[2]")
    Total_Leads = (By.XPATH, "//p[text() = 'Total Leads']")
    Number_Total_Leads = (By.XPATH, "//*[@id='dbData']/div[3]/a/div/div/h3")
    Unhandled_Fallbacks = (By.XPATH, "//p[text() = 'Unhandled Fallbacks']")
    Number_Unhandled_Fallbacks = (By.XPATH, "//*[@id='dbData']/div[4]/a/div/div/h3")
    Contact_Location = (By.CSS_SELECTOR, 'div#location_mapid')
    Chart_Dropdown = (By.CSS_SELECTOR, 'select#filterByGraph')
    Communication_Link = (By.XPATH, "//a[@href = '/chat']")
    End_Date_Calendar = (By.XPATH, "//div/input[@id = 'eDate']")
    Fallbacks = (By.XPATH, "//a[@href = '/fallbacks']")
    YourStory = (By.XPATH, "//a[@href = '/story']")
    Intent = (By.XPATH, "//a[@href = '/intent']")
    ConversationalFlow_Link = (By.XPATH, "//a[@href= '/tree']")
    Left_Menu_Links = (By.XPATH, "//section[@class = 'sidebar']//a[@href]")
    Help_LeftMenu = (By.XPATH, "//a[@href = '/help']")
    Integrations_Link = (By.XPATH, "//a[@href = '/integration']")
    Bot_Settings_Link = (By.XPATH, "//a[@href = '/subscription']")
    Slots_LeftMenu = (By.XPATH, "//a[@href = '/slots']")
    Webhook_And_Actions = (By.XPATH, "//a[@href = '/webhooks']")


    """Constructor of HomePage"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""

    def get_homepage_title(self, title):
        return self.get_title(title)

    def is_homePageLogo_visible(self):
        return self.is_element_displayed(self.Logo_HomePage)

    def is_leftMenu_DashboardLink_visible(self):
        return self.is_element_displayed(self.Dashboard_LeftMenu)

    def is_leftMenu_SignOutLink_visible(self):
        return self.is_visible(self.SignOut_LeftMenu)

    def click_leftMenu_SlotsLink(self):
        self.do_click(self.Slots_LeftMenu)
        return SlotsPage(self.driver)

    def click_leftMenu_Webhooks_and_Actions(self):
        self.do_click(self.Webhook_And_Actions)
        return WebhooksAndActions(self.driver)

    def click_editProfile_LeftMenu(self):
        self.do_click(self.EditProfile_LeftMenu)
        return EditProfilePage(self.driver)

    def do_SignOut(self):
        self.do_click(self.SignOut_LeftMenu)

    def get_all_Links_Status_Code(self):
        Links = self.get_all_elements(self.All_Links)

        for link in Links:
            request = requests.head(link.get_attribute('href'))
            requestStatusCode = str(request.status_code)
            return requestStatusCode

    def is_Dashboard_Elements_visible(self):

        if self.is_visible(self.Calendar_Range):
            if self.is_visible(self.Total_Conversation):
                if self.is_visible(self.No_of_Visitors):
                    if self.is_visible(self.Total_Leads):
                        if self.is_visible(self.Unhandled_Fallbacks):
                            if self.is_visible(self.Contact_Location):
                                print("All True")
                                return True

                            else:
                                return False

    def get_No_of_Conversation_dislayed(self):
        return self.get_element_text(self.Number_Total_Conversation)

    def get_No_of_Visitors_displayed(self):
        return self.get_element_text(self.Number_No_of_Visitors)

    def get_No_of_Total_Leads_displayed(self):
        return self.get_element_text(self.Number_Total_Leads)

    def get_No_of_unhandled_fallbacks(self):
        return self.get_element_text(self.Number_Unhandled_Fallbacks)

    def click_visitors_log_link(self):
        self.do_click(self.Visitors_Log_Link)
        return VisitorsLog(self.driver)

    def get_Chart_Filter_dropDown_Options(self):
        return self.select_by_dropdown(self.Chart_Dropdown)

    def click_communication_link(self):
        self.do_click(self.Communication_Link)
        return CommunicationPage(self.driver)

    def click_Calendar_Range(self):
        return self.is_clickable(self.Calendar_Range)

    def get_today_date(self):
        return self.get_current_date()

    def get_end_date_calendar(self):
        return self.get_element_attValue_javascript()

    def click_fallbacks_link(self):
        self.do_click(self.Fallbacks)
        return FallbacksPage(self.driver)

    def click_yourstory_link(self):
        self.do_click(self.YourStory)
        return YourStoryPage(self.driver)

    def click_help_link(self):
        self.do_click(self.Help_LeftMenu)
        return HelpPage(self.driver)

    def click_intent_link(self):
        self.do_click(self.Intent)
        return CreateIntentPage(self.driver)

    def click_conversational_flow_link(self):
        self.do_click(self.ConversationalFlow_Link)
        return ConversationalFlowPage(self.driver)

    def click_integration_link(self):
        self.do_click(self.Integrations_Link)
        return IntegrationsPage(self.driver)

    def click_bot_settings_link(self):
        self.do_click(self.Bot_Settings_Link)
        return BotSettingsPage(self.driver)

    def click_all_Links(self):
        Links = self.get_all_elements(self.Left_Menu_Links)
        win = len(self.driver.window_handles)
        i = 0
        while len(Links):
            if Links[i].text.strip() == 'Sign Out':
                Links[i].click()
                if win==1:
                    return True
                    break
                else:
                    return False

            else:
                Links[i].click()

                if win==1:

                    Links = self.get_all_elements(self.Left_Menu_Links)
                    i=i+1
                else:
                    return False


    def check_all_links_side_menu_visible(self):
        Links = self.get_all_elements(self.Left_Menu_Links)
        link_Name = Links[:]
        i = 0
        for link in Links:
            link_Name[i] = link.text.strip()
            i = i+1

        return link_Name

















