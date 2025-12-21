import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение деталей заказа: имя='{first_name}', "
                 "фамилия='{last_name}', индекс={postal_code}")
    def fill_order_details(self, first_name, last_name, postal_code):
        """
        Ожидание загрузки формы и ее заполнение

        :param first_name: str - имя покупателя

        :param last_name: str - фамилия покупателя

        :param postal_code: int - индекс
        """
        with allure.step("Ожидание загрузки формы оформления заказа"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )

        with allure.step(f"Заполнение поля имени: {first_name}"):
            first_name_field = self.driver.find_element(By.ID, "first-name")
            first_name_field.send_keys(first_name)

        with allure.step(f"Заполнение поля фамилии: {last_name}"):
            last_name_field = self.driver.find_element(By.ID, "last-name")
            last_name_field.send_keys(last_name)

        with allure.step(f"Заполнение поля почтового индекса: {postal_code}"):
            postal_code_field = self.driver.find_element(By.ID, "postal-code")
            postal_code_field.send_keys(postal_code)

        with allure.step("Нажатие кнопки Continue"):
            continue_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "continue"))
            )
            continue_button.click()

    @allure.step("Получение общей суммы заказа")
    def get_total_amount(self):
        """
        Получение и проверка суммы заказа

        :return: float
        """
        with allure.step("Ожидание отображения общей суммы заказа"):
            total_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "summary_total_label")))

        with allure.step("Извлечение текста с суммой"):
            total_text = total_element.text

        with allure.step("Преобразование текста в число"):
            # Избавляемся от всех символов, кроме чисел и десятичной точки
            cleaned_text = re.sub(r'[^\d\.]', '', total_text)
            # Преобразуем в вещественное число
            total_amount = float(cleaned_text)

        with allure.step("Возврат суммы заказа"):
            return total_amount