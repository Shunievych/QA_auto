from datetime import time

from page_objects.home_page import HomePage
from page_objects.registration_page import RegistrationPage
from page_objects.file_page import FilePage
from page_objects.garage_page import GaragePage

def test_create_user_add_car_and_expenses():
    driver =webdriver.Chome()

    home_page = HomePage(driver)
    home_page.open()
    home_page.click_sign_in_button()

    registration_page = RegistrationPage(driver)
    name = "TestName"
    last_name = "TestLastName"
    email = "tetiana.shunievych@gmail.com"
    password = "sh2800145ab"
    registration_page.register(name, last_name, email, password)

file_page = FilePage(driver)
assert file_page.get_name() == name
assert file_page.get_last_name() == last_name

#додати авто
garage_page = GaragePage(driver)
brand = "Porsche"
model = "911"
mileage = "10000"
garage_page.add_car(brand, model, mileage)

#видалити акаунт
garage_page.delete_account()

driver.quit()

time.sleep(20)


