from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.title = (By.CLASS_NAME, "title")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self):
        """Получение заголовка страницы"""
        return self.driver.find_element(*self.title).text

    def add_product_to_cart(self, product_name):
        """Добавление товара в корзину по названию"""
        # Локатор для кнопки добавления товара
        add_button_locator = (By.XPATH,
                              f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        add_button = self.wait.until(EC.element_to_be_clickable(add_button_locator))
        add_button.click()
        return self

    def get_cart_items_count(self):
        """Получение количества товаров в корзине"""
        try:
            badge = self.driver.find_element(*self.cart_badge)
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        """Переход в корзину"""
        cart_icon = self.driver.find_element(*self.cart_icon)
        cart_icon.click()