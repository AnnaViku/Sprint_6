import pytest
import allure
from selenium import webdriver
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from data.test_data import ORDER_DATA
from urls.urls import SCOOTER_URL

@pytest.mark.parametrize("name, phone", ORDER_DATA)
@allure.step("Проверка создания заказа с именем: {name} и телефоном: {phone}")
def test_order_creation(driver, name, phone):
    # Проверяем положительный сценарий для обеих кнопок
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    # Первый сценарий: нажать кнопку "Заказать" в верхней части страницы
    driver.get(SCOOTER_URL)
    main_page.click_order_button()
    order_page.fill_order_form(name, phone)
    order_page.submit_order()
    assert order_page.is_success_message_displayed()

    # Второй сценарий: нажать кнопку "Заказать" в нижней части страницы
    driver.get(SCOOTER_URL)
    main_page.click_order_button()
    order_page.fill_order_form(name, phone)
    order_page.submit_order()
    assert order_page.is_success_message_displayed()