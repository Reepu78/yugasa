# import time
#
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
#
# import self as self
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import geocoder
#
import random
import time

import geocoder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print(random.randint(1, 100))










# driver = webdriver.Chrome(executable_path="/Users/tshas/AutomationScenes/WebDrivers/ChromeDriver/chromedriver")
# driver.get("https://admin.helloyubo.com")
# driver.maximize_window()
# driver.find_element_by_id('username').send_keys('Testyubo')
# driver.find_element_by_id('password').send_keys('Test@123470')
# driver.find_element_by_id('submitBtn').click()
# driver.find_element_by_xpath("//a[@href= '/chat']").click()


# bot_url =driver.current_url
# second_driver = webdriver.Firefox()
# second_driver.get(bot_url)
# second_driver.maximize_window()
# print(bot_url)
#
# driver.find_element_by_link_text('Accept').is_displayed()
# # time.sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # All_Customer_Chat_Close_Btn = driver.find_element_by_xpath("(//button[@class = 'modal_close'])")
# driver.find_element_by_css_selector('button.btn.btn-primary.btn-xs.user').click()
#
# All_Cancel_Btns = driver.find_elements_by_xpath("//button[@class = 'modal_close']")
# second_cancel_btn = All_Cancel_Btns[1]
# second_cancel_btn.click()



# row = driver.find_element_by_css_selector("tr.tr2")
# num_Total_Rows = len(rows)
# Num_Total_Pages = num_Total_Rows/10  #1.3







# last_row = rows[-1]

# print(row.get_attribute('data-index'))



# driver.find_element_by_css_selector('button.btn.btn-primary.btn-xs.user').click()

# All_Customer_Chat_Close_Btn = driver.find_element_by_xpath("(//button[@class = 'modal_close'])")
# All_Cancel_Btns = driver.find_elements_by_xpath("(//button[@class = 'modal_close'])")
#
# driver.find_element(All_Cancel_Btns[1]).click()

# driver.execute_script("location.reload(true);")

# actions = ActionChains(driver)
# # actions.send_keys(Keys.COMMAND).send_keys(Keys.SHIFT).send_keys('R').perform()
# actions.send_keys(Keys.COMMAND).send_keys('F').perform()




# for _ in range(N):
#     actions = actions.send_keys(Keys.TAB)
# actions.send_keys('255')
#
# actions = actions.send_keys(Keys.TAB)
# actions.send_keys('0')
#
# actions = actions.send_keys(Keys.TAB)
# actions.send_keys('255')
#
# actions.send_keys(Keys.ENTER)
# actions.perform()


#
# driver.find_element_by_css_selector('input#dateRange').click()
# left_mon_year = driver.find_element_by_xpath("(//th[@class= 'month'])[1]").text
# print(left_mon_year)
#
# Expected_Left_Date = '3 May 2021'
# Expected_Left_Month_Year = Expected_Left_Date.split(" ")[1]+" "+Expected_Left_Date.split(" ")[2]
# Expected_Left_Month = Expected_Left_Date.split(" ")[1]
# Expected_Left_Year = Expected_Left_Date.split(" ")[2]
#
# if left_mon_year > Expected_Left_Month_Year.strip():
#     print("Values are great")

# i = int('30 may 2021')
# b = int('1 march 2022')
#
# if i>b:
#     print("a greater than c")
#


# values = ['3', '4', '4', '5', '6', '6', '6', '7', '8', '8', '9']
# # contains_duplicates = any(values.count(element) > 1 for element in values)
#
# a_set = set(values)
#
# contains_duplicates = len(values) != len(a_set)
#
# print(contains_duplicates)

# driver.find_element_by_xpath("//a[@href= '/subscription']").click()
# time.sleep(3)
# color_picker = driver.find_element_by_css_selector('input#headBgColor').click()
#
# N = 3  # number of times you want to press TAB
#



# # import requests
# # r = requests.get('https://api.ipdata.co?api-key=test').json()
# # r['country_name']
# # print(r)
#
# from ipregistry import IpregistryClient
# #
# client = IpregistryClient("tryout")
# ipInfo = client.lookup()
# print(ipInfo)
# g = geocoder.ip('me')
# print(g.latlng)
#
# driver = webdriver.Chrome(executable_path="/Users/tshas/AutomationScenes/WebDrivers/ChromeDriver/chromedriver")
# driver.get("https://admin.helloyubo.com/login")
# # time.sleep(5)
# action = ActionChains(driver)
# driver.find_element_by_id('username').send_keys('Testyubo')
# driver.find_element_by_id('password').send_keys('Test@123468')
# driver.find_element_by_id('submitBtn').click()
# # print(driver.current_url)
#
# driver.find_element_by_xpath("//a[@href= '/subscription']").click()
# time.sleep(3)
# color_picker = driver.find_element_by_css_selector('input#headBgColor').click()
#
# N = 3  # number of times you want to press TAB
#
# actions = ActionChains(driver)
# for _ in range(N):
#     actions = actions.send_keys(Keys.TAB)
# actions.send_keys('255')
#
# actions = actions.send_keys(Keys.TAB)
# actions.send_keys('0')
#
# actions = actions.send_keys(Keys.TAB)
# actions.send_keys('255')
#
# actions.send_keys(Keys.ENTER)
# actions.perform()
#
#
#
# # # action.move_to_element(self.get_element(by_locator)).perform()
# # self.do_click(self.Color_Picker)
# # action.send_keys(Keys.TAB)
#
# # time.sleep(5)
# # driver.find_element_by_xpath("//a[@href= '/subscription']").click()
# # time.sleep(5)
# # color_picker = driver.find_element_by_css_selector('input#headBgColor')
# # color_picker.send_keys("#0000FF")
# #
#
# # All_Links = (By.XPATH, "//a[@href]")
#
# # All_Links = driver.find_elements_by_xpath("//section[@class = 'sidebar']//a[@href]")
# #
# # for i in All_Links:
# #     i.click()
# #     win = len(driver.window_handles)
# #     time.sleep(5)
# #
# #     print(win)
# #     if win > 1:
# #         print("true")
# #     else:
# #         print("false")
#
#
#
#
#
# # driver.find_element_by_xpath("//a[@href= '/chat']").click()
# # time.sleep(10)
#
#
#
#
#
#
# from Config.TestData import TestData
# from Config.config import ConfigData
# from TestData import ExcelLogic
# from TestData.ExcelLogic import TestDataFromExcel
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # userName = (By.ID, 'username')
# # element = WebDriverWait(self, 10).until(EC.presence_of_element_located(userName))
# # print(element.is_displayed())
#
#
#
# # intentName = "Intent"+TestDataFromExcel.readIntentVariable(self)
# # intentName.strip()
# # varint = int(intentName.strip())+1
# #
# # print(varint)
#
#
# # intentName = TestDataFromExcel.readIntentVariable(self)
# # print(intentName)
# # print("-------")
# # string0 = intentName.split()[0]
# # print(string0)
# # string1 = str(int(intentName.split()[1])+1)
# # print(string1)
# #
# # print(string0 + " " + string1)
#
# # print(name[1])
# # varint = int(name)
# # print(varint)
#
#
#
# # print(driver.find_element_by_xpath("//tbody//tr[1]//td[6]").text)
# # from TestData.ExcelLogic import TestDataFromExcel
# #
# # TestDataFromExcel.newPassword_in_excel(2, 7, "value")
#
# # SelectAll_Checkbox = driver.find_element_by_css_selector("input.chkall")
# # all_chckbox = driver.find_elements_by_css_selector("input.chkbx")
# # SelectAll_Checkbox.click()
# # eles = all_chckbox[:]
# # for i in range(len(all_chckbox)):
# #     if SelectAll_Checkbox.is_selected():
# #             eles[i] = all_chckbox[i].is_selected()
# #             i = i + 1
# #     else:
# #         eles[i] = all_chckbox[i].is_selected()
# #         i = i + 1
# #
# #
# #
# # print(eles)
# #
#
#
# # SelectAll_Checkbox.click()
# # time.sleep(2)
# # SelectAll_Checkbox.click()
# # self.do_click(self.SelectAll_CheckBox)
# # if self.is_elememnt_selected(self.SelectAll_CheckBox):
# #     all_chckbox = self.get_all_elements(self.All_ChkBox_On_Page)
# #
# #     res = []
# #     for chckbox in all_chckbox:
# #         res = [self.is_elememnt_selected(chckbox)]
#
# #
# # if SelectAll_Checkbox.is_selected():
# #     res = []
# #
# #     for i in range(len(all_chckbox)):
# #         res = chckbox.is_selected()
# #
# #         # print(res)
# #
# #     print (res)
# #
#
#
# # eles = all_chckbox[:]
# # if SelectAll_Checkbox.is_selected():
# #     for i in range(len(all_chckbox)):
# #         if all_chckbox[i].is_selected():
# #             eles[i] = all_chckbox[i].is_selected()
# #             i= i +1
# #         elif not all_chckbox[i].is_selected():
# #             eles[i] = all_chckbox[i].is_selected()
# #             i = i + 1
# #
# #     print(eles)
#
#
#
# #
# #
#
#
# # all_Nodes = driver.find_elements_by_css_selector('div.ui-draggable')
# # for node in all_Nodes:
# #     node.click()
# #     break
# #
# # driver.find_element_by_css_selector('delete_selected_button').click()
#
# #  self.do_click(self.all_Nodes[0])
# # self.do_click(self.Delete_Btn)
# # return self.is_visible(self.Delete_Btn_PopUp_Head_Text)
#
# # lelement = driver.find_element_by_css_selector('img.width-eye-img')
# # ActionChains(driver).move_to_element(lelement).click().perform()
# #
# #
# # print(lelement.value_of_css_property('background-color'))
#
# # driver.find_element_by_id('dateRange').click()
#
# # time.sleep(5)
# # driver.find_element_by_css_selector("input.chkall").click()
# # time.sleep(2)
# # elements = driver.find_elements_by_css_selector('input.chkbx')
#
# # for i in range(len(elements)):
# #     if elements[i].is_selected():
# #         print(elements[i])
# #         i = i + 1
# #         print(i)
# #
# #     else:
# #         print("Failed")
# # eles = elements[:]
# #
# # for i in range(len(elements)):
# #     if elements[i].is_selected():
# #         i = i + 1
# #     else:
# #         print("Failed")
# #
# # print(all(eles))
#
#
# # left_monthYearVal = driver.find_element_by_xpath("//div[@class = 'drp-calendar left']//th[@class = 'month']").text
# # print(left_monthYearVal)
# #
# # Month = left_monthYearVal.split()[0].strip()
# # Year = left_monthYearVal.split()[1].strip()
# # print(Month)
# # print(Year)
# #
# # while (Month != 'Jan' and Year != 2021):
# #     driver.find_element_by_css_selector("th.prev.available").click()
# #     left_monthYearVal = driver.find_element_by_xpath("//div[@class = 'drp-calendar left']//th[@class = 'month']").text
# #     Month = left_monthYearVal.split()[0].strip()
# #     Year = left_monthYearVal.split()[1].strip()
# #     print(left_monthYearVal)
# #
# # driver.find_element_by_xpath("//div[@class = 'drp-calendar left']//td[text() = '23']").click()
# #
#
# # def get_left_Month_year(left_monthYearVal):
# #     return left_monthYearVal.split()
# #
# # def select_date(day , month , year):
# #     left_monthYearVal = driver.find_element_by_xpath("//div[@class = 'drp-calendar left']//th[@class = 'month']").text
# #     print(left_monthYearVal)
# #
# #     while (get_left_Month_year(left_monthYearVal)[0] != month and get_left_Month_year(left_monthYearVal)[1] != year):
# #         driver.find_element_by_css_selector("th.prev.available").click()
# #         left_monthYearVal = driver.find_element_by_xpath("//div[@class = 'drp-calendar left']//th[@class = 'month']").text
# #
# #     driver.find_element_by_xpath("//div[@class = 'drp-calendar left']//td[text() = '"+day+"']").click()
# #
# #
# #
# #
# # select_date('14' , 'June', '2020')
#
#
# # find broken links
# # links = driver.find_elements(By.CSS_SELECTOR, "a")
# # valid_links = 0
# # broken_links = 0
# # for link in links:
# #     try:
# #         request = requests.head(link.get_attribute('href'), data={'key': 'value'})
# #         print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
# #
# #         if (request.status_code == 404):
# #             broken_links = (broken_links + 1)
# #         else:
# #             valid_links = (valid_links + 1)
# #     except requests.exceptions.MissingSchema:
# #         print("Encountered MissingSchema Exception")
# #     except requests.exceptions.InvalidSchema:
# #         print("Encountered InvalidSchema Exception")
# #     except:
# #         print("Encountered Some other execption")
# #
# # print("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(valid_links) + " valid links")
#
# # sideBarLinks = driver.find_elements_by_xpath("//section[@class = 'sidebar']/ul")
# # time.sleep(10)
# #
# # for link in sideBarLinks:
# #      link.click()
# #      print(link)
# #      time.sleep(10)
# #
# # def dropdownelements():
# #     select = Select(driver.find_element_by_css_selector('select#filterByGraph'))
# #     dropdown_Options = select.options
# #
# #     for option in dropdown_Options:
# #         actual_DropDown_val = [option.text]
# #
# #         return actual_DropDown_val
# #
# # def expecteddropdownele():
# #
# #      return expectedlIst
# #
# #
# # def comparelist():
# #     print(dropdownelements())
#
# #
# # if os.path.exists('filename.csv'):
# #     print("File exist")
# # else:
# #     print("File not exist")
#
# # for option in dropdown_Options:
# #
# #    return val
#
#
# # def find_select_by_dropDown():
# #    print(select_by_dropDown)
#
# # current_Date = datetime.datetime.now()
# # Month = datetime.datetime.now().month
# # Date = datetime.datetime.now().day
# # Year = datetime.datetime.now().year
# # print(str(Date).strip())
# # print(current_Date)
# # print("--------")
# # print(str(current_Date.strftime("%d/%m/%Y")))
# #
# # print(str(current_Date).rstrip())
# # print (str(Date).lstrip(), str(Month).rstrip() , str(Year).lstrip())
#
# #
# # Calendar = driver.find_element_by_xpath("//div/input[@id = 'eDate']")
# #
# # print(driver.execute_script('return document.getElementById("eDate").value'))
