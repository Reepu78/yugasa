import datetime
import os
import os.path

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from Config.config import ConfigData

"""This class is parent of all pages"""
"""Contains all generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def is_clickable(self, by_locator):
        flag = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(flag)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def is_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()

        except TimeoutException:
            return False

    def clear_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        return element

    def get_element_attribute(self, by_locator, att_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(att_name)

    def get_element_attValue_javascript(self):
        return self.driver.execute_script('return document.getElementById("eDate").value')

    # def refresh_page(self):
    #     self.driver.


    def get_pseudo_element(self):
        script = "document.querySelector('.fa-trash-o'), '::before'"
        # self.driver.execute_script("arguments[0].click(); ", script)
        self.driver.execute_script("arguments[0].click(); ", script)


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_box_color(self, by_locator, cssProperty):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.value_of_css_property(cssProperty)

    def is_element_enable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_enabled()

    def select_by_dropdown(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        select = Select(element)
        dropdown_Options = select.options

        actual_dropDown_val = dropdown_Options[:]
        i = 0

        for option in dropdown_Options:
            actual_dropDown_val[i] = option.text
            i = i + 1

        return actual_dropDown_val

    def get_all_elements(self, by_locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(by_locator))


    def is_file_exist(self, file_path):
        flag = os.path.isfile(file_path)
        return flag

    def get_current_date(self):
        current_Date = datetime.datetime.now()
        return str(current_Date.strftime("%d/%m/%Y"))

    def elements_are_selected(self, by_locator, selectAll_Checkbox):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        eles = elements[:]

        for i in range(len(elements)):
            if self.is_element_selected(selectAll_Checkbox):
                eles[i] = elements[i].is_selected()
                i = i + 1
            else:
                eles[i] = elements[i].is_selected()
                i = i + 1

        return all(eles)

    def element_mouse_hover(self, by_locator):
        ActionChains(self.driver).move_to_element(self.get_element(by_locator)).perform()

    def do_hard_refresh(self):
        self.driver.execute_script("location.reload(true);")

    def get_countof_elements_in_list(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return len(elements)

    def is_element_selected(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_selected()

    def click_first_element_from_elements(self, by_locator):
        elements = self.get_all_elements(by_locator)
        for element in len(elements):
            self.get_element(element).click()

    def select_dates_in_calendar(self, Expected_Left_Date, Expected_Right_Date):
        Expected_Left_Date = Expected_Left_Date
        Expected_Right_Date = Expected_Right_Date

        Expected_Left_Month_Year = (Expected_Left_Date.split(" ")[1] + " " + Expected_Left_Date.split(" ")[2]).strip()
        Expected_Left_Day = Expected_Left_Date.split(" ")[0].strip()

        Expected_Right_Day = Expected_Right_Date.split(" ")[0].strip()
        Expected_Right_Month_Year = (Expected_Right_Date.split(" ")[1] + " " + Expected_Right_Date.split(" ")[2]).strip()

        Actual_Left_Month_Year = self.get_element_text(self.Left_Month_Year_Value)
        Actual_Right_Month_Year = self.get_element_text(self.Right_Month_Year_Value)

        while Expected_Left_Month_Year != Actual_Left_Month_Year:
            self.do_click(self.Calendar_Back_BTN)
            Actual_Left_Month_Year = self.get_element_text(self.Left_Month_Year_Value)

        Left_Days = self.get_all_elements(self.Calendar_Left_Day)
        for Day in Left_Days:
            if Day.text == Expected_Left_Day:
                Day.click()
                break

        if Expected_Left_Month_Year == Expected_Right_Month_Year:
            self.do_click(self.Calendar_Back_BTN)
            Right_Days = self.get_all_elements(self.Calendar_Right_Day)
            for Day in Right_Days:
                if Day.text == Expected_Right_Day:
                    Day.click()
                    break
        else:
            Actual_Right_Month_Year = self.get_element_text(self.Right_Month_Year_Value)

            while Expected_Right_Month_Year != Actual_Right_Month_Year:
                self.do_click(self.Calendar_Next_Btn)
                Actual_Right_Month_Year = self.get_element_text(self.Right_Month_Year_Value)

            Right_Days = self.get_all_elements(self.Calendar_Right_Day)
            for Day in Right_Days:
                if Day.text == Expected_Right_Day:
                    Day.click()
                    break

    def take_screenshot(self):
        self.driver.get_screenshot_as_file(ConfigData.SCREENSHOTS_FOLDER + "Screenshots.png")