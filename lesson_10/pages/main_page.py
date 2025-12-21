import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.add_backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bolt_tshirt_btn = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товаров в корзину")
    def add_items_to_cart(self):
        """
        Добавление товаров в корзину

        :return: None
        """
        with allure.step("Добавление рюкзака 'Sauce Labs Backpack' в корзину"):
            self.driver.find_element(*self.add_backpack_btn).click()

        with allure.step("Добавление футболки 'Sauce Labs Bolt T-Shirt' "
                         "в корзину"):
            self.driver.find_element(*self.add_bolt_tshirt_btn).click()

        with allure.step("Добавление комбинезона 'Sauce Labs Onesie' "
                         "в корзину"):
            self.driver.find_element(*self.add_onesie_btn).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переход на страницу корзины путем нажатия по иконке корзины

        :return: None
        """
        with allure.step("Нажатие на иконку корзины"):
            self.driver.find_element(*self.cart_icon).click()

        with allure.step("Ожидание перехода на страницу корзины"):
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/cart.html"))