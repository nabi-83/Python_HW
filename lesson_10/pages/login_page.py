import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Загрузка страницы авторизации")
    def load(self):
        """
        Загрузка главной страницы сайта

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод учетных данных: пользователь='{username}, {password}'")
    def enter_credentials(self, username, password):
        """
        Ввод имени и пароля

        :param username: str - имя пользователя

        :param password: str - пароль

        :return: None
        """
        with allure.step(f"Ввод имени пользователя: {username}"):
            user_input = self.driver.find_element(*self.username_field)
            user_input.send_keys(username)

        with allure.step(f"Ввод пароля: {password}"):
            pass_input = self.driver.find_element(*self.password_field)
            pass_input.send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def click_login(self):
        """
        Инициация процесса авторизации путем нажатия кнопки входа

        :return: None
        """
        with allure.step("Поиск кнопки Login"):
            btn = self.driver.find_element(*self.login_button)

        with allure.step("Нажатие кнопки входа"):
            btn.click()

    @allure.step("Ожидание перехода на домашнюю страницу")
    def wait_for_homepage(self):
        """
        Ожидание изменения url страницы

        :return: None
        """
        with allure.step("Ожидание URL, содержащего '/inventory.html'"):
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/inventory.html"))