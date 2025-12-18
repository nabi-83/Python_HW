from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.title = (By.CLASS_NAME, "title")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")

    def get_title(self):
        """Получение заголовка страницы корзины"""
        return self.driver.find_element(*self.title).text

    def get_cart_items_count(self):
        """Получение количества товаров в корзине"""
        items = self.driver.find_elements(*self.cart_items)
        return len(items)

    def get_cart_item_names(self):
        """Получение названий всех товаров в корзине"""
        items = self.driver.find_elements(*self.cart_items)
        item_names = []
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            item_names.append(name_element.text)
        return item_names

    def click_checkout(self):
        """Нажатие кнопки Checkout"""
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout_btn.click()