import pytest
from selenium import webdriver
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage

@pytest.mark.parametrize("name, phone", [
    ("Иван Иванов", "+79012345678"),
    ("Петр Петров", "+79098765432"),
])
def test_order_creation(name, phone):
    driver = webdriver.Chrome()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.click_order_button()
    order_page.fill_order_form(name, phone)
    order_page.submit_order()

    assert order_page.is_success_message_displayed()
    driver.quit()