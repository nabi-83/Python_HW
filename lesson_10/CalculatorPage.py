import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открытие страницы
        """
        with allure.step("Переход по URL калькулятора"):
            self.driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "slow-calculator.html")

    @allure.step("Установка задержки вычислений: {seconds} секунд")
    def set_delay(self, seconds):
        """
        Установка задержки вычислений

        :param seconds: int — время задержки в секундах
        """
        with allure.step("Очистка поля задержки"):
            delay_input = self.driver.find_element(By.ID, 'delay')
            delay_input.clear()
        with allure.step(f"Ввод значения {seconds} в поле задержки"):
            delay_input.send_keys(str(seconds))

    @allure.step("Нажатие кнопки: '{button_text}'")
    def click_button(self, button_text):
        """
        Нажатие кнопки калькулятора по её текстовому содержимому

        :param button_text: str - текст на кнопке
        """
        with allure.step(f"Поиск кнопки с текстом '{button_text}'"):
            button = self.driver.find_element(
                By.XPATH, f"//span[text()='{button_text}']")

        with allure.step(f"Клик по кнопке '{button_text}'"):
            button.click()

    @allure.step("Вычисление выражения: {expression}")
    def calculate_expression(self, expression):
        """
        Вычисление выражения

        :param expression: str - выражение для расчёта
        """
        with allure.step(f"Последовательное нажатие кнопок для "
                         f"выражения: {expression}"):
            for char in expression:
                self.click_button(char)

        with allure.step("Нажатие кнопки '=' для выполнения вычисления"):
            self.click_button('=')  # Нажимаем равно

    @allure.step("Получение результата вычисления")
    def get_result(self):
        """
        Получение результата вычисления
        """
        with allure.step("Поиск элемента с результатом"):
            result_element = self.driver.find_element(By.CLASS_NAME, "screen")

        with allure.step("Получение текста результата"):
            return result_element.text.strip()

    @allure.step("Ожидание результата: {expected_value}")
    def wait_until_result_is(self, expected_value):
        """
        Ожидаем пока результат станет равным ожидаемому значению

        :param expected_value: int - ожидаемое значение
        """
        with allure.step(f"Ожидание появления результата {expected_value} на "
                         "экране"):
            self.wait.until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "screen"), str(expected_value))
            )