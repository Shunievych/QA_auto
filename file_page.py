from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class FilePage(BasePage):

    def get_name(self):
        return self._driver.find_element(By.ID, 'userName').text

    def get_last_name(self):
        return self._driver.find_element(By.ID, 'userLastName').text


