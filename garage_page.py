from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class GaragePage(BasePage):

    def add_car(self, brand, model, mileage):
        self._driver.find_element(By.XPATH, "//button[contains(te[t(),'Add Car')]").click()
        self._driver.find_element(By.ID, 'addCarBrand').send_key(brand)
        self._driver.find_element(By.ID, 'addCarModel').send_key(model)
        self._driver.find_element(By.ID, 'addCarMileage').send_key(mileage)
        self._driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]").click()


