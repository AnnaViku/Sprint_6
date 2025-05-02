from selenium.webdriver.common.by import By

class OrderPage:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Введите имя']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Введите телефон']")
    BUTTON_SUBMIT = (By.XPATH, "//button[text()='Завершить']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ создан')]")

    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, name, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def submit_order(self):
        self.driver.find_element(*self.BUTTON_SUBMIT).click()

    def is_success_message_displayed(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()