from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class RegistrationPage(BasePage):
    def register(self, name, last_name, email, password):
        self._driver.find_element(By.ID, 'name').send_keys(name)
        self._driver.find_element(By.ID, 'lastName').send_keys(last_name)
        self._driver.find_element(By.ID,'email').send_keys(email)
        self._driver.find_element(By.ID, 'password').send_keys(password)
        self._driver.find_element(By.ID, 'repeatPassword').send_keys(password)
        self._driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").click()




