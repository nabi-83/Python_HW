from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main():
    # Инициализация драйвера Edge
    driver = webdriver.Edge()

    try:
        # Переход на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполнение формы
        driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

        # Нажатие кнопки Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        # Ожидание применения стилей после отправки формы
        wait = WebDriverWait(driver, 10)

        # Проверка, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code должно быть подсвечено красным"

        # Проверка, что остальные поля подсвечены зеленым
        fields_to_check = [
            'first-name',
            'last-name',
            'address',
            'e-mail',
            'phone',
            'city',
            'country',
            'job-position',
            'company'
        ]

        for field_id in fields_to_check:
            field = driver.find_element(By.CSS_SELECTOR, f'#{field_id}')
            assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} должно быть подсвечено зеленым"

        print("Все проверки пройдены успешно!")

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()