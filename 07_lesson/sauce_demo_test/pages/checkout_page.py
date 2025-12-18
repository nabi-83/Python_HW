from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.title = (By.CLASS_NAME, "title")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def get_title(self):
        """Получение заголовка страницы"""
        return self.driver.find_element(*self.title).text

    def enter_first_name(self, first_name):
        """Ввод имени"""
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.first_name_input))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        """Ввод фамилии"""
        last_name_field = self.driver.find_element(*self.last_name_input)
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        """Ввод почтового индекса"""
        postal_code_field = self.driver.find_element(*self.postal_code_input)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        return self

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Заполнение всей информации для оформления заказа"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    def click_continue(self):
        """Нажатие кнопки Continue"""
        continue_btn = self.driver.find_element(*self.continue_button)
        continue_btn.click()