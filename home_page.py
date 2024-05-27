from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class HomePage(BasePage):
    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def click_sign_in_button(self):
        self._driver.find_element(By.XPATH, "//body/app-root/app-global-layout/div[@class='global-layout']//app-heder//button[@class='btn btn-outline-white header_signin").click()


