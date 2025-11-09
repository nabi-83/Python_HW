from selenium.webdriver.common.by import By
import re


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы
        self.title = (By.CLASS_NAME, "title")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def get_title(self):
        """Получение заголовка страницы"""
        return self.driver.find_element(*self.title).text

    def get_total(self):
        """Получение итоговой суммы"""
        total_text = self.driver.find_element(*self.total_label).text
        return self._extract_price(total_text)

    def _extract_price(self, text):
        """Извлечение цены из текста"""
        price_match = re.search(r'\$([\d.]+)', text)
        if price_match:
            return float(price_match.group(1))
        return 0.0