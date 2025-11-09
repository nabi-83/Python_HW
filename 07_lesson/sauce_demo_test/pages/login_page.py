from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        """Открытие страницы авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        """Ввод имени пользователя"""
        username_field = self.wait.until(EC.element_to_be_clickable(self.username_input))
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        """Ввод пароля"""
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        """Нажатие кнопки Login"""
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()

    def login(self, username, password):
        """Полный процесс авторизации"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()