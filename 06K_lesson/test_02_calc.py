from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Переход на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 50)  # Увеличиваем общее время ожидания до 50 секунд

        # Ввод значения 45 в поле задержки
        delay_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажатие кнопок: 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидание появления результата 15
        # Ждем до 46 секунд (45 + 1 секунда запаса)
        result_display = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"),
            message="Результат 15 не появился в течение 45 секунд"
        )

        # Дополнительная проверка результата
        final_result = driver.find_element(By.CLASS_NAME, "screen").text
        assert final_result == "15", f"Ожидался результат 15, но получили {final_result}"

        print("Тест пройден успешно! Результат 15 отобразился через 45 секунд.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()