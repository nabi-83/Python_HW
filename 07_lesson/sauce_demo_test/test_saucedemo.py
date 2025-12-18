import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        # Настройка ChromeOptions
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # Режим инкогнито
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()

        # Инициализация Page Objects
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_overview_page = CheckoutOverviewPage(self.driver)

    def test_complete_purchase_flow(self):
        """Тест полного процесса покупки"""
        # Шаг 1: Открытие сайта и авторизация
        self.login_page.open().login("standard_user", "secret_sauce")

        # Проверка успешной авторизации
        self.assertEqual("Products", self.products_page.get_title())

        # Шаг 2: Добавление товаров в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product in products_to_add:
            self.products_page.add_product_to_cart(product)

        # Проверка количества товаров в корзине
        self.assertEqual(3, self.products_page.get_cart_items_count())

        # Шаг 3: Переход в корзину
        self.products_page.go_to_cart()

        # Проверка перехода в корзину
        self.assertEqual("Your Cart", self.cart_page.get_title())

        # Проверка товаров в корзине
        cart_items = self.cart_page.get_cart_item_names()
        self.assertEqual(3, len(cart_items))
        for product in products_to_add:
            self.assertIn(product, cart_items)

        # Шаг 4: Нажатие кнопки Checkout
        self.cart_page.click_checkout()

        # Проверка перехода на страницу оформления заказа
        self.assertEqual("Checkout: Your Information", self.checkout_page.get_title())

        # Шаг 5: Заполнение формы данными
        self.checkout_page.fill_checkout_info("Ирина", "Бухарина", "456804")
        self.checkout_page.click_continue()

        # Проверка перехода на страницу обзора заказа
        self.assertEqual("Checkout: Overview", self.checkout_overview_page.get_title())

        # Шаг 6: Проверка итоговой стоимости
        total_amount = self.checkout_overview_page.get_total()

        # Проверка что итоговая сумма равна $58.29
        self.assertEqual(58.29, total_amount,
                         f"Итоговая сумма должна быть $58.29, но получена ${total_amount}")

    def tearDown(self):
        """Действия после каждого теста"""
        if self.driver:
            self.driver.quit()