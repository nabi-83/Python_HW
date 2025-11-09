from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_sauce_demo_purchase():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        # Создаем объект ожидания
        wait = WebDriverWait(driver, 10)

        # Переход на сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизация как пользователь standard_user
        username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Ожидание загрузки страницы товаров
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Добавление товаров в корзину
        # Sauce Labs Backpack
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()

        # Sauce Labs Bolt T-Shirt
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()

        # Sauce Labs Onesie
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()

        # Переход в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Ожидание загрузки страницы корзины
        wait.until(EC.presence_of_element_located((By.ID, "cart_contents_container")))

        # Нажатие кнопки Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Ожидание загрузки формы checkout
        wait.until(EC.presence_of_element_located((By.ID, "checkout_info_container")))

        # Заполнение формы своими данными
        first_name_field = driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Ирина")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Бухарина")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("456804")

        # Нажатие кнопки Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Ожидание загрузки страницы с итоговой стоимостью
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

        # Чтение итоговой стоимости
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")

        # Проверка, что итоговая сумма равна $58.29
        assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получили ${total_amount}"

        print(f"Тест пройден успешно! Итоговая сумма: ${total_amount}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_sauce_demo_purchase()