import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Переход на страницу оформления заказа")
    def proceed_to_checkout(self):
        """
        Переход на страницу оформления заказа в корзине покупок
        """
        with allure.step("Нажатие кнопки 'Checkout'"):
            self.driver.find_element(*self.checkout_button).click()

        with allure.step("Ожидание перехода на страницу оформления заказа"):
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/checkout-step-one.html"))