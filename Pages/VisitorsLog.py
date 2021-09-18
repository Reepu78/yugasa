from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class VisitorsLog(BasePage):

    """Page Actions"""
    Total_Rows= (By.CSS_SELECTOR, 'tr.tr2')



    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""
    def count_total_rows(self):
        rows = self.get_all_elements(self.Total_Rows)
        return len(rows)



