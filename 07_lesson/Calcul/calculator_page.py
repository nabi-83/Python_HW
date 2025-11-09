from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)  # Увеличиваем время ожидания до 50 секунд

        # Локаторы элементов
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.equals_button = (By.XPATH, "//span[text()='=']")

    def set_delay(self, delay_value):
        """Установка значения задержки в поле ввода"""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(delay_value)

    def click_button(self, button_text):
        """Нажатие кнопки с указанным текстом"""
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def perform_addition(self):
        """Выполнение операции 7 + 8"""
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    def get_result(self):
        """Получение результата с ожиданием"""
        try:
            # Ждем, пока результат не станет равным "15"
            self.wait.until(
                EC.text_to_be_present_in_element(self.result_display, "15")
            )

            result_element = self.driver.find_element(*self.result_display)
            return result_element.text
        except TimeoutException:
            # Если время ожидания истекло, возвращаем текущий текст
            result_element = self.driver.find_element(*self.result_display)
            return result_element.text

    def get_display_text(self):
        """Получение текущего текста с экрана (без ожидания)"""
        display = self.driver.find_element(*self.result_display)
        return display.text

    def wait_for_calculation(self, timeout=50):
        """Ожидание завершения расчета с проверкой результата"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            current_text = self.get_display_text()
            if current_text == "15":
                return True
            time.sleep(0.5)  # Проверяем каждые 500 мс

        return False