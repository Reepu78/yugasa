import logging
import os
from datetime import datetime
from logging import error
from urllib import request

import pytest
import webdriver_manager
from _pytest.fixtures import fixture
from webdriver_manager import driver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

from Config.config import ConfigData
from selenium import webdriver

from TestData.ExcelLogic import TestDataFromExcel
from Pages.BasePage import BasePage

global web_driver


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):

    global web_driver

    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # web_driver = webdriver.Chrome(executable_path='c:\Automation\YugasaLabs\driver\chromedriver.exe', options=chrome_options)
        web_driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    if request.param == 'ie':
        web_driver = webdriver.Ie(executable_path=IEDriverManager().install())

    if request.param == 'edge':
        web_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    if request.param == 'safari':
        web_driver = webdriver.Safari()

    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.quit()


# @fixture(scope='function')
# def hard_refresh():
#     BasePage.do_hard_refresh()
#     print("\nreseting")
#
@pytest.fixture(autouse=True)
def hard_refresh():
    web_driver.execute_script("location.reload(true);")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # basePage = BasePage(driver)
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         web_driver.get_screenshot_as_file(ConfigData.SCREENSHOTS_FOLDER + str(item)+"_"+str(now)+".png")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # basePage = BasePage(driver)
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        tcName = str(item)
        cheklst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for char in tcName:
            if not char.lower() in cheklst:
                tcName = tcName.replace(char, '_')
        web_driver.get_screenshot_as_file(ConfigData.SCREENSHOTS_FOLDER + tcName+str(now)+".png")


# # confest.Theme function defined py
# def _fail_picture():
#     webdriver.fail_picture()
#
#  # Write the hook function
#  # Failure use of an automatic function screenshot
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#          hook pytest failure
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         _fail_picture()
#

