import allure
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@allure.feature("Процесс покупки")
@pytest.fixture(scope="session")
def browser():
    """
    Инициализация и завершение работы браузера
    """
    with allure.step("Инициализация браузера Firefox"):
        driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()))
        yield driver

    with allure.step("Завершение работы браузера"):
        driver.quit()


@pytest.mark.usefixtures("browser")
class TestShopFlow:
    @allure.title("Тест процесса онлайн-покупки")
    @allure.description("Тестирование полного цикла покупки: от авторизации "
                        "до оформления заказа с проверкой итоговой суммы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shopping_flow(self, browser):
        """
        Тестирование процесса покупки:
        1. Авторизация с корректными учетными данными
        2. Добавление трех товаров в корзину, переход в корзину
        3. Подтверждение и переход к оформлению заказа
        4. Оформление заказа с заполнением данных доставки
        5. Проверка корректности итоговой суммы

        :param browser: str - Объект браузера из фикстуры

        :return: None
        """

        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        with allure.step("ШАГ 1: Авторизация в системе"):
            with allure.step("Загрузка страницы авторизации"):
                login_page.load()

            with allure.step("Ввод учетных данных пользователя"):
                login_page.enter_credentials("standard_user", "secret_sauce")

            with allure.step("Нажатие кнопки входа"):
                login_page.click_login()

            with allure.step("Ожидание перехода на главную страницу"):
                login_page.wait_for_homepage()

        with allure.step("ШАГ 2: Добавление товаров в корзину"):
            with allure.step("Добавление трех товаров в корзину"):
                main_page.add_items_to_cart()

            with allure.step("Переход в корзину"):
                main_page.go_to_cart()

        with allure.step("ШАГ 3: Переход к оформлению заказа"):
            with allure.step("Нажатие кнопки Checkout"):
                cart_page.proceed_to_checkout()

        with allure.step("ШАГ 4: Оформление заказа"):
            with allure.step("Заполнение данных для доставки"):
                checkout_page.fill_order_details("Ирина", "Бухарина", "456804")

        with allure.step("ШАГ 5: Проверка итоговой суммы заказа"):
            with allure.step("Получение общей суммы заказа"):
                total_amount = checkout_page.get_total_amount()

            with allure.step("Проверка соответствия ожидаемой сумме"):
                assert total_amount == 58.29