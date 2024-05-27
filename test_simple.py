import pytest

from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
   driver = webdriver.Chrome()
   yield driver
   driver.close()

@pytest.fixture()
def go_to_home_page(driver):
   driver.get("https://www.selenium.dev")

def test_title_is_correct(driver, go_to_home_page):
   assert driver.title == "Selenium"

   def test_main_text_is_present(driver, go_to_home_page):
      element = driver.find_element(By.TAG_NAME, 'h1')
      assert element.text == "Selenium automates browsers. That's it!"

      def test_selenium_support_section_is_present(driver, go_to_home_page):
         element = driver.find_element(By.XPATH, "//h2[contains(.,'Donate to Selenium')]")
         assert element.is_displayed()


